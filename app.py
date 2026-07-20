import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="StudyGPT",
    page_icon="📚",
    layout="wide"
)

st.title("📚 StudyGPT")
st.subheader("AI Study Assistant")

upload_folder = Path("data/uploads")
upload_folder.mkdir(parents=True, exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload your study material",
    type=["pdf"]
)

if uploaded_file is not None:
    file_path = upload_folder / uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded successfully!")

    st.write("Filename:", uploaded_file.name)

    st.write("Saved at:", file_path)