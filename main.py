import requests
from bs4 import BeautifulSoup

url = "https://www.xataka.com/espacio/nasa-va-a-recortar-presupuesto-hubble-su-salvacion-pasa-dos-multimillonarios-sector-privado"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Obtener el título de la página
title = soup.title.string
print("Título:")
print(title)

# Obtener los li con la clase deseada
li_tags = soup.find_all('li', class_='masthead-nav-topics-item')
print("Etiquetas <li> con la clase:")
for li in li_tags:
    print(li)

# Obtener el texto limpio de la noticia
article_content = soup.find('div', class_='article-content')
if article_content:
    # Eliminar todas las etiquetas <em>
    for em in article_content.find_all('em'):
        em.decompose()
        
    article_text = article_content.get_text(strip=True)
    print("Texto limpio de la noticia:")
    print(article_text)
else:
    print("No se ha encontrado el texto de la noticia.")