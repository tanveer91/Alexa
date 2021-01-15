import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listen = sr.Recognizer()
speak = pyttsx3.init()
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[2].id)


def talk(text):
    speak.say(text)
    speak.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listen.listen(source)
            command = listen.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('it is' + time)
    elif 'who' or 'tell' in command:
        wiki = command.replace('who', '')
        wiki = command.replace('tell', '')
        info = wikipedia.summary(wiki, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run()
