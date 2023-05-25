import streamlit as st
import speech_recognition as sr
import requests

text_input = st.text_input("Enter your text here:")

voice_input = st.button("Speak")

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        SpeechToText = r.recognize_google(audio, language='en-in')

    except Exception:
        st.write("Say that again please...")  
        return None
    
    return SpeechToText



API_URL = "https://api-inference.huggingface.co/models/APP04/codeparrot"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	


if voice_input:
   text_input = takeCommand()
   output = query({
	"inputs": text_input
})
   st.write(output)

else:
     output = query({
	"inputs": text_input})
     st.write(output)


