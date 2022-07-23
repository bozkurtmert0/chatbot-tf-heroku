import streamlit as st
from streamlit_chat import message as st_message
from chatbot import response, bot_name


st.set_page_config(
    page_title="AI- Kevin",
    page_icon=":robot:"
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title(bot_name)

def ol():
    user_message = st.session_state.input_text
    res= response(user_message)
    st.session_state.history.append({"message": user_message, "is_user": True})
    st.session_state.history.append({"message": res, "is_user": False})

#user_message = st.session_state.input_text
#result = model.generate(**inputs)

st.text_input("Tell me something", key="input_text", on_change=ol)

for chat in st.session_state.history:
    st_message(**chat)  # unpacking
