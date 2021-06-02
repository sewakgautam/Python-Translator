import speech_recognition as sr
import pyttsx3
from googletrans import Translator

print("Evi is listening........")
# Initialize the recognizer 
r = sr.Recognizer()
translator = Translator()

def speak(command):
    
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    engine.stop()

def listen():
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2, duration=0.2)
        audio2 = r.listen(source2)
        MyText = r.recognize_google(audio2)
        MyText = MyText.lower()
        print("Evi is listening........")
        print("Did you say "+MyText)
        
        speak(MyText)
        translate(MyText)
    

def translate(command):
    result = translator.translate(command, src='en', dest='ne')
    print(result.text)
    speak(result.text)
listen()
