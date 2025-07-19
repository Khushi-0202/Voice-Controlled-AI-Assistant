import pyttsx3
import datetime
import speech_recognition as sr #pip install speechrecognition
import wikipedia
import webbrowser
import os
'''import smtplib'''

engine= pyttsx3.init('sapi5')
#sapi5 is used to take voices frm the cmoputer the inbuilt voice inside the laptop.
voices= engine.getProperty('voices')
# print(voices) This will return us how many voices are already present in our system.
engine.setProperty('voice',voices[1].id)

def speak(audio):
#speak function takes the string and speaks it
    engine.say(audio)
    engine.runAndWait()

def wishMe():
#wishes the author according to the time of the day
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am AI , how may I help you?")

def takeCommand():
    #it takes microphone I/P from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "none"
    return query

'''def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close() '''

if __name__=="__main__":
    wishMe()
    while True:
    #if 1:
        query=takeCommand().lower()
    
    #logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query=query.replace("wikipedia","") #removes the word wikipedia from the given microphone input and searches the rest on wikipedia
            results=wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir= 'D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        ''' elif 'email to khushi' in query:
            try:
                speak("What should  say?")
                content=takeCommand()
                to="khushiyouremail.gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send the email at this moment") '''