import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyB8hSNq9l9aP_dN7F6fdmcsCkuTg3vDO5s"

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    convert_system_message_to_human=True
)

# ✅ Use simple instruction prompt (fixes your issue)
prompt = PromptTemplate.from_template("Translate this into French:\n\n{input_text}")

# Chain
translation_chain: Runnable = prompt | llm

# Streamlit UI
st.set_page_config(page_title="English to French Translator")
st.title("🌍 English to French Translator")
st.markdown("Translate English sentences into French using Google Gemini via LangChain.")

# Input
user_input = st.text_input("Enter an English sentence:")

if st.button("Translate"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a sentence.")
    else:
        try:
            result = translation_chain.invoke({"input_text": user_input})
            translated_text = result.content if hasattr(result, "content") else str(result)
            st.success("✅ Translation Successful!")
            st.markdown(f"**French Translation:**\n\n> {translated_text}")
        except Exception as e:
            st.error(f"❌ Error during translation:\n\n{e}")
