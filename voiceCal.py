import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    '''This function speaks the Text which is passed in audio argument'''
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    """Returns string output from microphone"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=10)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user: {query}")
    except:
        speak("Say That again please")
        return "None"
    return query


def options():
    speak("Which kind of operation would you like to perform?")
    speak("Addition, subtraction, multiplication or division")  
    speak("Say Exit for close the calculator")



if __name__ == '__main__':
    speak("Hello There! welcome to the voice calculator developed by, Nishant The Programmer")
    notExit = True
    while(notExit):
        options()
        command = takeCommand()
        if "exit" in command:
            speak("Thank's for using our voice calculator!")
            break

        elif "add" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                speak(f"Addition of {a} and {b} is " + str(a + b))
            except:
                speak("Sorry try again!")
        elif "subtraction" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                speak(f"{a} minus {b} is " + str(a - b))
            except:
                speak("Sorry try again!")
        elif "multi" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                speak(f"Multiplication of {a} and {b} is " + str(a * b))
            except:
                speak("Sorry try again!")
        elif "div" in command:
            try:
                speak("What is your first operand?")
                a = int(takeCommand())
                speak("What is your second operand?")
                b = int(takeCommand())
                if(b == 0):
                    speak("As all we know any value divide by zero is undefined so please give a valid second operand next time, Thanks!")
                    continue
                
                speak(f"{a} divide by {b} is " + str(a / b))
            except:
                speak("Sorry try again!")
    