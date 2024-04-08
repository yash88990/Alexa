#  Importing Libraries:...
import speech_recognition as sr   
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

#  Setting Up Speech Recognition and Text-to-Speech Engine:
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening .....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command: 
                command = command.replace('alexa','')   
                print(command)
    except:
        pass
    return command 

def run_alexa():
    command = take_command()
    print(command)
    if 'play ' in command :
        song = command.replace('play' , '')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command :
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time )
    elif 'tell me about' in command:
        person = command.replace('tell me about','').strip()
        person = person.replace(' ' , '_')
        print("searching for : " , person)
        try:
            info = wikipedia.summary(person, sentences=1)
            print(info)
            talk(info)
        except wikipedia.exceptions.PageError:
            print(f"Sorry, I couldn't find information about {person} on Wikipedia.")
            talk(f"Sorry, I couldn't find information about {person} on Wikipedia.")
    elif 'date' in command:
        talk('sorry , i  have a headache ')
    elif 'are you single ' in command :
        talk('i am in a relationship with yash chaudhary')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again ')

while True:
    run_alexa()

