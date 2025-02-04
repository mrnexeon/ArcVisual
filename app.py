import streamlit as st

# Title of the app
st.title("My Basic Streamlit App")

# Some text
st.write("Hello, world! This is my first Streamlit app.")

# Add a simple interactive widget
user_input = st.text_input("Enter some text", "Type here...")
st.write("You entered:", user_input)
