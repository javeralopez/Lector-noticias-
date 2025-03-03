import streamlit as st
import requests
from bs4 import BeautifulSoup

# Título de la aplicación
st.title("Web Scraping con Streamlit")

# Input para la URL
url = st.text_input("Introduce la URL de la página web que quieres scrapear:")

def scrape_website(url):
    try:
        # Hacer la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP

        # Parsear el contenido de la página con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraer el título de la página
        page_title = soup.title.string if soup.title else "No se encontró el título"
        st.write(f"**Título de la página:** {page_title}")

        # Extraer todos los enlaces (etiquetas <a>)
        links = soup.find_all('a')
        if links:
            st.write("**Enlaces encontrados:**")
            for link in links:
                href = link.get('href')
                text = link.get_text(strip=True)
                st.write(f"- {text}: {href}")
        else:
            st.write("No se encontraron enlaces en la página.")

        # Extraer texto de la página (opcional)
        if st.checkbox("Mostrar texto de la página"):
            page_text = soup.get_text()
            st.write("**Texto de la página:**")
            st.write(page_text)

    except requests.exceptions.RequestException as e:
        st.error(f"Error al acceder a la página: {e}")
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")

if url:
    scrape_website(url)
else:
    st.write("Por favor, introduce una URL válida.")