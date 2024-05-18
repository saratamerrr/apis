import streamlit as st
import requests
import json
from pprint import pprint

# Title and description
st.title("Astronauts in Space")
st.markdown("This app shows the current number of people in space and their names, as well as the current location of the ISS.")

# Get astronauts data
astro_response = requests.get("http://api.open-notify.org/astros.json")
astro_data = astro_response.json()

# Display the number of people in space
st.subheader(f"Number of people in space: {astro_data['number']}")

# Display astronaut names
st.subheader("Names of the astronauts:")
for person in astro_data['people']:
    st.write(person['name'])

# Get ISS current location
iss_response = requests.get("http://api.open-notify.org/iss-now.json")
iss_data = iss_response.json()

# Display ISS location
iss_position = iss_data['iss_position']
latitude = iss_position['latitude']
longitude = iss_position['longitude']

st.subheader("Current location of the ISS:")
st.write(f"Latitude: {latitude}")
st.write(f"Longitude: {longitude}")

# Display the ISS location on a map
st.map(data={'lat': [float(latitude)], 'lon': [float(longitude)]})

