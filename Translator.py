import streamlit as st
from googletrans import Translator

# Language List for Dropdowns
LANGUAGES = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Hindi": "hi",
    "Bengali": "bn",
    "Urdu": "ur",
    "Tamil": "ta",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Punjabi": "pa",
    "Thai": "th",
    "Vietnamese": "vi",
    "Indonesian": "id",
    "Turkish": "tr",
    "Greek": "el",
    "Dutch": "nl",
    "Polish": "pl",
    "Hebrew": "he",
    "Swahili": "sw",
}

# Translator object
translator = Translator()

# Streamlit App
def main():
    # Page title
    st.set_page_config(
        page_title="Multi-Language Translator",
        page_icon="🌐",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS with animations
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            background: linear-gradient(to right, #1c1c1c, #3a6073, #2a5298);
            font-family: 'Roboto', sans-serif;
            color: #ecf0f1;
        }
        .stApp {
            background-color: rgba(44, 62, 80, 0.9);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            animation: fadeIn 2s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        h1 {
            color: #f39c12;
            text-align: center;
            animation: slideIn 1s;
        }
        @keyframes slideIn {
            from { transform: translateY(-50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .stButton>button {
            background-color: #1abc9c;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px;
            transition: transform 0.2s;
        }
        .stButton>button:hover {
            background-color: #16a085;
            transform: scale(1.1);
        }
        textarea {
            background-color: #34495e;
            border-radius: 10px;
            border: 1px solid #2c3e50;
            padding: 10px;
            font-size: 16px;
            color: #ecf0f1;
        }
        .stAlert {
            background-color: #e74c3c;
            border: 1px solid #c0392b;
            border-radius: 5px;
        }
        footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Animated Header
    st.title("🌐 Multi-Language Translator")
    st.markdown("<div style='text-align: center;'>Translate text between 30+ languages with animations! 🎉</div>", unsafe_allow_html=True)

    # Input Section
    st.subheader("Enter Text to Translate")
    input_text = st.text_area(
        "Input your text here 👇",
        placeholder="Type the text you want to translate...",
        height=150,
    )

    # Language Selection
    col1, col2 = st.columns(2)

    with col1:
        source_lang = st.selectbox("Select Source Language 🌎", options=list(LANGUAGES.keys()))

    with col2:
        target_lang = st.selectbox("Select Target Language 🗺️", options=list(LANGUAGES.keys()))

    # Translate Button
    if st.button("Translate 🔄"):
        if input_text.strip() == "":
            st.error("❗ Please enter text to translate!")
        elif source_lang == target_lang:
            st.warning("❗ Source and Target languages cannot be the same.")
        else:
            with st.spinner("Translating... 🔄"):
                try:
                    # Translation process
                    translated_text = translator.translate(
                        input_text, src=LANGUAGES[source_lang], dest=LANGUAGES[target_lang]
                    )
                    # Display translation
                    st.success("🎉 Translation Successful!")
                    st.subheader("Translated Text")
                    st.text_area(
                        "Translation Output",
                        value=translated_text.text,
                        height=150,
                    )
                except Exception as e:
                    st.error(f"❗ An error occurred during translation: {e}")

    # Footer Section
    st.markdown(
        """
        <div style='text-align: center; margin-top: 50px;'>
            <p style='color: #bdc3c7;'>🌟 Language data powered by Google Translate.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
