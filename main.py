import streamlit as st
from streamlit_chat import message
import requests

url = "https://open-ai21.p.rapidapi.com/conversationmpt"

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "7df7b083fcmsh694ab47253d50d0p1e3073jsnfd8c802e325a",
	"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
}

def generate_response(prompt):
    try:
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "web_access": False
        }
        print(payload)
        response = requests.post(url, json=payload, headers=headers)
        # print(response.json())
        print(response.json())
        return response.json()['MPT']
    except Exception as e:
        print("Probably rate limit")
        return None

def get_input():
    global value
    input_text = st.text_input("CN Bot:",  key="input", placeholder="Type")
    print("inp: ",input_text)
    return input_text



st.title("ChatBot")

changes = '''
<style>
[data-testid = "stAppViewContainer"]
{
background-image: url('https://images.unsplash.com/photo-1475274047050-1d0c0975c63e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=872&q=80');
background-size: cover;
}

</style>
'''
st.markdown(changes, unsafe_allow_html=True)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []


user_input = get_input()

payload = {
	"messages": [
		{
			"role": "user",
			"content": user_input
		}
	],
	"web_access": False
}
if user_input:
    # print(user_input)
    output = generate_response(user_input)
    print("Response", output)
    if output:
        # print(output)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], key="user_" + str(i), is_user=True)


