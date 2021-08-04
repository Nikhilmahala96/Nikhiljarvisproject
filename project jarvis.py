import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning nikhil")
    elif hour>=12 and hour<=17:
        speak("Good afternoon nikhil")
    else:
        speak("Good evening ")

    speak("hello Nikhil sir . I am jarvis , how may i help  you")
def takecommand():
    #it take microphone  input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.........")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ =='__main__':
    wishme()
    speak("I can play movies , open google , gmail and youtube , can search on wikipedia too")
    while True:
        query = takecommand().lower()

    #logic for excecuting task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 1)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open mail' in query:
            webbrowser.open("gmail.com")

        elif 'uit rgpv' in query:
            webbrowser.open("uitrgpv.ac.in")


        elif' play movies ' in query:
            movies_dir = 'C:\\Users\\HP\\Desktop\\movie\\new film'
            movies = os.listdir(movies_dir)
            print(movies)
            os.startfile(os.path.join(movies_dir,movies[0]))

        elif 'open code ' in query:
            webbrowser.open("w3schools.com")







