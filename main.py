import streamlit as st
import requests

# Assign API key and url.
api_key = "k039QewgO4acK6ZGpdEZJXtav7KvewCamIkSzJk0"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# Make requests to get JSON
request = requests.get(url)
content = request.json()

# Display header, img, and description.
st.header("Galaxy by the Lake")
st.image(content["url"])
st.write(content["explanation"])



