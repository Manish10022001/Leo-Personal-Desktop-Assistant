import pywhatkit
import pyttsx3
import datetime
import speech_recognition
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os 
from datetime import timedelta
from datetime import datetime
import time

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
        if "stop" in query.lower():
            speak("Stopping the program.")
            exit()
        return query.lower()
    except Exception as e:
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime("%H"))
##pywhatkit.core.exceptions.CallTimeException: Call Time must be Greater than Wait Time as WhatsApp Web takes some Time to Load!
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))

def sendMessage():
    speak("Who do you wan to message")
    ##a = int(input('''Manish - 1
    ##Suresh - 2'''))
    person_name = takeCommand().lower()
    if person_name=='manish':
        speak("Whats the message")
        message = takeCommand()
        
        pywhatkit.sendwhatmsg("+918806903085",message,time_hour=strTime,time_min=update) 
   
    elif "Suresh" in person_name:
        speak("Whats the message")
        message = takeCommand()
        pywhatkit.sendwhatmsg("+918888344404",message,time_hour=strTime,time_min=update)
       

    sendMessage()