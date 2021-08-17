import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from tkinter import *
import random
from datetime import datetime
now = datetime.now()
# dd/mm/YY H:M:S
date = datetime. now(). strftime("%Y_%m_%d-%I_%M_%S_%p")
file="Audio"+str(date)
code = random. randint(0,1000)

print("Your Audio file while be saved with the code",code)
print("Start giving your input as soon as you press the START button")
print("For how many seconds would you speak approximately")
n=int(input())
def Voice_rec():
    fs = 48000
    duration = n
    myrecording = sd.rec(int(duration * fs), 
                         samplerate=fs, channels=2)
    sd.wait()
    sf.write(str(code)+".flac", myrecording, fs)
    audiofile=(str(code)+".flac")
    r=sr.Recognizer()      #initialize the recognizer
    with sr.AudioFile(audiofile) as source:
        audio=r.record(source)

    try:
        query=r.recognize_google(audio)
        print("The content of the audio file is " + r.recognize_google(audio))
    except sr.UnknownValueError :
        print("Google speech Recognition could not understand audio")
    except sr.RequestError :
        print("Couldnt get the result from google speech recognition")
  
    
    filename=code
    with open(str(filename)+'.txt', 'a') as f:
         f.write(query)
  
  
master = Tk()
Label(master, text=" Voice Recoder : ").grid(row=0, sticky=W, rowspan=5)
b = Button(master, text="Start", command=Voice_rec)
b.grid(row=0, column=2, columnspan=2, rowspan=2,
       padx=5, pady=5)
  
mainloop()


