import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("Text Summarizer")

user_text = st.text_area("Write your text here")

if st.button("Summarize"):
    if user_text.strip():
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize this text:\n\n{user_text}"
                }
            ]
        )

        summary = response.choices[0].message.content

        st.write("Summarized text:")
        st.write(summary)

    else:
        st.warning("Please enter some text to summarize.")
