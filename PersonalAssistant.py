# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:19:24 2018

@author: Manav
"""

#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
#from gtts import gTTS
import webbrowser
import platform
syss=platform.system()
if syss=='Windows':
    import win32com.client as wincl
    speakss = wincl.Dispatch("SAPI.SpVoice")

def speak(audioString):
    print(audioString)
    speakss.Speak(audioString)
 
    
#this part is for listening.....
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes am listening!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "forget you" in data:
        speak("aww.. so kind of you. Thank you")
    if "close" in data or "bye" in data:
        speak("Thank you for choosing me as your assistant. See you soon...")
        os._exit(0)
    if "how are you" in data:
        speak("I am fine and you ?")
    if "good" in data:
        speak("great")
    if "what time is it" in data:
        speak(ctime())
    if "miss you" in data or "missed you" in data:
        speak("I miss you too.. ")
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on for a second, I will show you where " + location + " is.")
        #os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
 
# initialization
time.sleep(2)
speak("Hi. May I know your name please:")
name=recordAudio()
speak("Hi "+name+", thats very good name. So do you know my name ? Please call my name. ")
while 1:
    
    data = recordAudio()
    if "sandy" in data or "Sandy" in data:
        speak("Yeah... You remembered me ...")
        while 1:
            data = recordAudio()
            jarvis(data)
    else:
        speak("You forgot me.. This is not done. Please call my name. ")


 

