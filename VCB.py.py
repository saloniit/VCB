import pyttsx3
import speech_recognition as s
import datetime
import wikipedia as wi
import webbrowser as web
import smtplib as sm

from wikipedia.wikipedia import summary
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.stop()
def wish():
    h=int(datetime.datetime.now().hour)
    if(0<=h<12):
        speak("Good Morning Sir!")
    elif(12<=h<18):
        speak("Good afternoon Sir")
    elif(18<=h<22):
        speak("Good evening Sir")
    else:
        speak("Good night Sir!")
def command():
    r=s.Recognizer()
    with s.Microphone() as source:
        print("Listening...")
        r.energy_threshold=500
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
        return query.lower()
    except Exception:

        print("voice cannot recognize please say again..")
        speak("voice cannot recognize please say again..")
        return "None"
def email(content,sender):
    f=open("G:\abcd.txt")
    p=f.read()
   
    server=sm.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('chowdhuryrahul197@gmail.com',p)
    server.sendmail("chowdhuryrahul197@gmail.com",sender,content)
    server.close()


wish()
print("I am alexa,  how may I help you")
speak("I am alexa,  how may I help you")
c=command()

while(True):
    if(c==None):
        c=command()
        continue
    elif("browser" in c):
        print("say site name")
        speak("say site name")
        z=command()
        web.open(f"https://www.{z}.com/")
    elif(c in "alexa shutdown"):
        speak("have a nice day,  Bye Bye!!")
        print("shut down!!")
        quit()
    elif("wikipedia" in c):
        print("what are you looking for!!")
        speak("what are you looking for!!")
        c=command()
        try:
            print("finding please wait..")
            speak("finding please wait..")
            r=wi.summary(c, sentences=2)
            print(r)
            speak(r)
        except Exception:
            print(" sorry sir could not find any thing that you are looking for!!")
            speak("sorry sir could not find any thing!!")
    elif('mail' in c):
        try:
            print("please write the sender email")
            speak("please write the sender email")
            e=input()
            print("please speak the content")
            speak("please speak the content")
            content=command()
            email(content,e)
            speak("mail send successfully")
        except Exception:
            print("due to bad network email does not send!!")
            speak("due to bad network email does not send!!")
    else:
        speak("could not find anything that you are looking for")
        speak("please say again")
    print("waiting for your command sir..!")
    speak("waiting for your command sir..!")
    c=command()
    
    




