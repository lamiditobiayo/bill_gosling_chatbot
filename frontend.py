import streamlit as st
import requests

st.set_page_config(page_title="Bill Gosling AI Chatbot", layout="wide")

st.title("💬 Bill Gosling AI Chatbot")
st.write("Ask me anything about Bill Gosling Outsourcing!")

user_input = st.text_input("You:", "", key="input", help="Type your message and press Enter")

if st.button("Send") or (user_input and st.session_state.get("enter_pressed")):
    st.session_state.enter_pressed = False  # Reset enter key press

    if user_input:
        with st.spinner("Thinking..."):
            response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_input})

            if response.status_code == 200:
                st.text_area("Chatbot:", response.json()["response"], height=150)
            else:
                st.error("Error: " + response.json().get("error", "Something went wrong"))

st.markdown("---")
st.write("Developed by [Tobi Lamidi](https://www.billgosling.com/)")

# Add Enter Keypress Support
def enter_keypress():
    st.session_state.enter_pressed = True

st.text_input("", "", key="enter_press", on_change=enter_keypress)
