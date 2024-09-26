
import streamlit as st
from PIL import Image
import easyocr
import numpy as np

# Function to perform OCR
def extract_text(image):
    """Extract text from image using EasyOCR."""
    reader = easyocr.Reader(['en', 'hi'])  # Specify languages
    result = reader.readtext(image)
    text = " ".join([r[1] for r in result])  # Extract text from result
    return text

# Streamlit application
st.title("OCR Text Extraction and Keyword Search")

# Upload image
uploaded_file = st.file_uploader("Upload an image (JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Convert image to NumPy array
    image_np = np.array(image)

    # Perform OCR
    extracted_text = extract_text(image_np)
    st.subheader("Extracted Text:")
    st.write(extracted_text)

    # Keyword search
    keyword = st.text_input("Enter keyword to search:")
    
    if keyword:
        results = [line for line in extracted_text.splitlines() if keyword.lower() in line.lower()]
        st.subheader("Search Results:")
        if results:
            for result in results:
                st.write(f"• {result}")
        else:
            st.write("No matches found.")
