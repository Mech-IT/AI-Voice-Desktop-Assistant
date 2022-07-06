import pyttsx3
import datetime
import requests
import json
import time
import requests
import wikipedia
import webbrowser
import os
import smtplib
import rsa
def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 160)
    engine.say(text)
    engine.runAndWait()
def wishme(hour):
    if 0<= hour < 12:
        speak("Good morning sir")
        speak("Hello sir how can i help you?")
    elif 12<= hour < 18:
        speak("Good afternoon sir")
        speak("Hello sir how can i help you?")
    else:
        speak("Good evening sir")
        speak("Hello sir how can i help you?")

def command():
    import speech_recognition as sr

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Listening.... ')
        audio = r.listen(source)

        try:
            global query
            query = r.recognize_google(audio)
            print(f"User Said:{query.lower()}")
        except:
            print('Sorry could not hear')
            print("please speak again")
            query=""

def news():
    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey= YOUR API KEY')
    a = json.loads((r.text))
    m = "sir so our today's top news are as follows."
    n = "Thanks for listening "
    li = (a["articles"])
    for i in range(1, (len(li) + 1)):
        if i == 1:
            print(m)
            speak(m)
            speak(f"news{i}")
            h = li[i - 1]["title"]
            v = li[i - 1]["url"]
            print(h)
            print(v)
            speak(h)
            continue
        elif i == len(li):
            speak(f"news{len(li)}")
            h = li[i - 1]["title"]
            v = li[i - 1]["url"]
            print(h)
            print(v)
            speak(h)
            print(n)
            speak(n)
            continue
        else:
            speak(f"news{i}")
            h = li[i - 1]["title"]
            v = li[i - 1]["url"]
            print(h)
            print(v)
            speak(h)
            continue
def search():
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    # to search
    quert = query.replace("search","")

    for j in search(quert, tld="co.in", num=10, stop=10, pause=2):
        print(j)


if __name__ == '__main__':
    wishme(datetime.datetime.now().hour)
    while(True):
                    command()
                    if "wikipedia" in query.lower():
                        speak("searching wikipedia")
                        title= query.replace("wikipedia","")
                        result = wikipedia.summary(title,sentences=2)
                        speak("According to wikipedia")
                        print(result)
                        speak(result)

                    elif "open website" in query.lower():
                        web=query.replace("open website","")
                        webbrowser.open(web)

                    elif " time" in query.lower():
                        speak(f"Sir the time is{datetime.datetime.now()}")

                    elif "open code" in query.lower():
                        path="FULL PATH OF YOUR VS CODE EDITOR"
                        os.startfile(path)
                        
                    elif "news" in query.lower():
                        news()
                    elif "search" in query.lower():
                        search()

                    elif "quit" in query.lower():
                        speak("whenever you need help please call me I am always available for your assistance, Thank you!")
                        exit()


































