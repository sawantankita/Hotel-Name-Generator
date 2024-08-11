import streamlit as st
import random

def generate_hotel_name(cuisine, theme, location):
    cuisine_adjectives = {
        'Indian': ['Spice', 'Curry', 'Masala', 'Royal'],
        'Chinese': ['Dragon', 'Lotus', 'Zen', 'Golden'],
        'Italian': ['Bella', 'Vino', 'Tuscan', 'Amore'],
        'Mexican': ['Fiesta', 'Sol', 'Aztec', 'El Dorado'],
        'French': ['Château', 'Bistro', 'Riviera', 'Étoile'],
        'Japanese': ['Sakura', 'Samurai', 'Zen', 'Koi']
    }

    theme_adjectives = {
        'Luxury': ['Grand', 'Palace', 'Imperial', 'Elegance'],
        'Budget': ['Comfort', 'Easy', 'Smart', 'Simple'],
        'Boutique': ['Unique', 'Chic', 'Artisan', 'Vintage'],
        'Eco-friendly': ['Green', 'Sustainable', 'Eco', 'Nature'],
        'Modern': ['Urban', 'Metro', 'Contempo', 'Fusion'],
        'Traditional': ['Heritage', 'Classic', 'Colonial', 'Rustic']
    }

    location_suffix = location if location else random.choice(['Inn', 'Hotel', 'Resort', 'Retreat'])

    name = f"{random.choice(cuisine_adjectives[cuisine])} {random.choice(theme_adjectives[theme])} {location_suffix}"
    return name

st.title("Hotel Name Generator")

st.sidebar.header("Customize Your Hotel Name")

cuisine = st.sidebar.selectbox("Pick a cuisine:", ['Indian', 'Chinese', 'Italian', 'Mexican', 'French', 'Japanese'])

theme = st.sidebar.selectbox("Pick a theme:", ['Luxury', 'Budget', 'Boutique', 'Eco-friendly', 'Modern', 'Traditional'])

location = st.sidebar.text_input("Enter location (optional):", "")

if st.sidebar.button("Generate Hotel Name"):
    hotel_name = generate_hotel_name(cuisine, theme, location)

    st.subheader("Suggested Hotel Name")
    st.write(hotel_name)
