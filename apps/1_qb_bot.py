from dotenv import load_dotenv
load_dotenv(override=True)
import streamlit as st



from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.title("Askbuddy -  AI QnA bot")
st.markdown("My QnA Bot with Langchain and Google Gemini")

if "message" not in st.session_state:
    st.session_state.message = []

for message in st.session_state.message:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)




query = st.chat_input("Ask anything?")
if query:
    st.session_state.message.append({"role":"User","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.message.append({"role":"ai","content":res.content})