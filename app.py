# app.py
import streamlit as st
from rag_pipeline import get_conversational_chain

st.set_page_config(page_title="🍲 Lost Recipe Reconstructor", layout="centered")
st.title("🍲 Lost Recipe Reconstructor (Chatbot)")
st.markdown("Describe a vague recipe memory and chat to refine it!")

if "chain" not in st.session_state:
    st.session_state.chain = get_conversational_chain()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Tell me about that old mango pickle recipe...")

if user_input:
    response = st.session_state.chain.run(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")
