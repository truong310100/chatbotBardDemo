from bardapi import Bard #pip install bardapi
import streamlit as st #pip install streamlit
from streamlit_chat import message #pip install streamlit_chat
import os

os.environ["_BARD_API_KEY"]="cwi3PezlwfOrj7TpZKzXiV1CuApH4HXBMM1zjVR5R34HfWLWlr7PkvlkxCGzJIE574CiTA."
st.title("Bot Hung Hau")

def response_API(promot):
    message=Bard().get_answer(str(promot))['content']
    return message

def user_input():
    input_text = st.text_input("Aa")
    return input_text

if 'generate' not in st.session_state:
    st.session_state['generate']=[]
if 'past' not in st.session_state:
    st.session_state['past']=[]

user_text = user_input()

if user_text:
    output = response_API(user_text)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate']) -1, -1, -1):
        message(st.session_state["past"][i], is_user=True, key = str(i) + '_user')
        message(st.session_state["generate"][i], key = str(i))

# run code: "streamlit run botBard.py"