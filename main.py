import speech_recognition as sr
import pyttsx3
import random
import datetime
import time as t
import webbrowser
import wikipedia
import csv
import os
import cv2
import pyaudio
import playsound
from PIL import ImageTk,Image
import tkinter as ttk
import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging

from google_speech import Speech

# logging.basicConfig(level=logging.INFO)


chatbot = ChatBot('e bot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    'chatterbot.corpus.english'

)
data=json.load(open('nfL6.json','r'))
train=[]
for row in data:
    train.append(row["question"])
    train.append(row["answer"])
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot=ChatBot("e bot")
trainer=ListTrainer(chatbot)
# trainer.train(train[:10])

def chat():
    com_speak("From now all reply will be automatic! To exit just say stop...")
    while True:
        res = get_command()
        if "stop" in res:
            com_speak("Now you are back in main fram...")
            break
        response = chatbot.get_response(res)
        response=str(response)
        com_speak(response)

window=ttk.Tk()
window.title("e bot")

var1=ttk.StringVar()
var2=ttk.StringVar()
var3=ttk.StringVar()

wish_msg="""I am your bot! My name is ebot !I am here to help you """

n_sound="Ahh ! Ahh Uhh Ahhhh!"
cute="I am a cute cute mini robot... Pleace give me love"


GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up","hey"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

f=open("jokes.csv","r")
reader=csv.reader(f)
jocks=[]
for row in reader:
    jocks.append(row[1])

def com_speak(audio):
    var2.set(audio)
    window.update()
    lang = "en"
    speech = Speech(audio, lang)
    speech.play()
    var2.set("....")
    window.update()

def user_speak(txt):
    var1.set(txt)
    window.update()

def get_command():
    r=sr.Recognizer()
    r.pause_threshold=0.8
    r.energy_threshold=300
    with sr.Microphone() as source:
        var3.set("Lisenting...")
        window.update()
        audio=r.listen(source)
        var3.set("Reconizeing....Wait.....")
        window.update()
    try:
        quary=r.recognize_google(audio,language="en-in")
    except:
        return "None"
    user_speak(quary)
    return str(quary.lower())

def wish_me():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        com_speak("Good Morning!Fahim !")
    elif hour>=12 and hour<18:
        com_speak("Good Evening!Fahim !")
    elif hour>=18 and hour<24:
        com_speak("Good Night!Fahim !")
    else:
        com_speak("It's deep night you should sleep now!")
    com_speak(wish_msg)


def os_path(path):
    com_speak("Opening File....")
    os.startfile(path)

def rock_paper_sizer():
    com_speak("Say Rock or Paper or Sizer..")
    com_turn=["rock","paper","sizer"]
    x=random.randint(0,2)
    com_case=com_turn[x]
    while True:
        user_term=get_command()
        if user_term[0]=="r":
            com_speak(f"Computer Chose {com_case}....")
            user_term="rock"
            break
        elif user_term[0]=="p":
            com_speak(f"Computer Chose {com_case}....")
            user_term="paper"
            break
        elif user_term[0]=='s' or user_term[0]=='c':
            com_speak(f"Computer Chose {com_case}...")
            user_term="sizer"
            break
        else:
            com_speak("Sorry I could not get pleace say again...")
    if com_case==user_term:
         com_speak("It is a tie!!!")
    else:
        if user_term=="rock" and com_case=="sizer":
            com_speak("Hurray You Win!!!")
        elif user_term=="paper" and com_case=="rock":
            com_speak("Hurray You Win!!!")
        elif user_term=="sizer" and com_case=="paper":
            com_speak("Hurray You Win!!!")
        else:
            com_speak("Sad You lose!!!")

def num_guse():
    num_try=0
    num_x=str(5)
    com_speak("Guees any number between 1 to ten.Maximum 3 chance")
    ply_num=get_command().lower()
    for i in range(3):
        if num_x==ply_num:
            num_try=10-(i*3)
            com_speak("Yo Bro you win the game")
            break
        else:
            com_speak("Sorry answer did not match. Try again!")
            com_speak(f"Guees any number between 1 to ten.Left {3-(1+i)} chance")
            ply_num=get_command().lower()

    com_speak(f"Your Score {num_try}")


def camera():
    cap=cv2.VideoCapture(0)
    out=cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
    while True:
        _,frame=cap.read()
        out.write(frame)
        cv2.imshow("Camrea",frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    out.release()
    cap.release()
    cv2.destroyAllWindows()


def play():
    but_2["state"]="disable"
    wish_me()
    while True:
        quary=get_command()
        quary=quary.lower()
        print(quary)
        if "stop" in quary or "exit" in quary:
            com_speak("Program Shutdown")
            var1.set("You Said...")
            var2.set("Com Said...")
            var3.set("....")
            window.update()
            but_2["state"] = "normal"
            break

        elif "talk" in quary:
            chat()

        elif "time" in quary:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            com_speak(time)
        elif "my wife" in quary:
            print("Ema Wastion")
            com_speak("Ema Wastion")

        elif "my name" in quary:
            print(f"Your name is Fahim")
            com_speak(f"Your name is Fahim")

        elif "my age" in quary:
            print(f"Your age is 20")
            com_speak(f"Your name is 20")

        elif "what is your name" in quary:
            print(wish_msg)
            com_speak(wish_msg)
        elif "create you" in quary:
            print("Fahim create me")
            com_speak("Fahim create me")
        elif "camera" in quary:
            camera()
        elif "number game" in quary:
            num_guse()
        elif "rock" in quary:
            rock_paper_sizer()

        elif "chrome" in quary:
            want_run = 'google-chrome'
            os.system('bash -c ' + want_run)

        elif "pycharm" in quary:
            want_run = 'pycharm-professional'
            os.system('bash -c ' + want_run)

        elif "vs" in quary:
            want_run = 'code'
            os.system('bash -c ' + want_run)

        elif "wikipedia" in quary:
            com_speak("Searching Wikipedia...")
            while True:
                try:
                    quary=quary.replace("wikipedia","")
                    result=wikipedia.summary(quary,sentences=1)
                    print(result)
                    com_speak(result)
                    break
                except:
                    com_speak("Sorry too many match.Can not find...")
                    break

        elif "open youtube" in quary:
            want_run = 'google-chrome www.youtube.com'
            os.system('bash -c ' + want_run)

        elif "open google" in quary:
            want_run = 'google-chrome www.google.com'
            os.system('bash -c ' + want_run)

        elif "open facebook" in quary:
            want_run = 'google-chrome www.facebook.com'
            os.system('bash -c ' + want_run)

        elif "music" in quary:
            want_run = 'rhythmbox && rhythmbox-client --play Resume playback if currently paused'
            os.system('bash -c ' + want_run)

        elif "open instagram" in quary:
            want_run = 'google-chrome www.instagram.com'
            os.system('bash -c ' + want_run)

        elif "joke" in quary:
            a=random.randint(0,len(jocks)-1)
            print(jocks[a])
            com_speak(jocks[a])

        elif "n sound" in quary:
            print(n_sound)
            com_speak(n_sound)

        elif quary in GREETING_INPUTS:
            a=random.randint(0,len(GREETING_RESPONSES)-1)
            print(GREETING_RESPONSES[a])
            com_speak(GREETING_RESPONSES[a])
        elif "who" in quary or "what" in quary:
            while True:
                try:
                    result = wikipedia.summary(quary, sentences=1)
                    print(result)
                    com_speak(result)
                    var1.set("....")
                    window.update()
                    break
                except:
                    com_speak("Sorry I can not found that...")
                    break
        elif quary==None:
            com_speak("Sorry I could not get pleace say again...")

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

frames = [ttk.PhotoImage(file='abstract_mech_dribble_2.gif',format = 'gif -index %i' %(i)) for i in range(200)]

window.geometry("1400x1000")
label = ttk.Label(window, width = 400, height = 200)
label.pack()
window.after(0, update, 0)

uni_text_label=ttk.Label(window,textvariable=var3)
var3.set(".....")
uni_text_label.configure(height=5,width=100)
uni_text_label.config(font=("Courier", 10))
uni_text_label.pack()

user_text_label=ttk.Label(window,textvariable=var1)
var1.set("You said: ")
user_text_label.configure(height=5,width=100)
user_text_label.config(font=("Courier", 10))
user_text_label.pack()

com_text_label=ttk.Label(window,textvariable=var2)
var2.set("Comp Said: ")
com_text_label.configure(height=5,width=300)
com_text_label.config(font=("Courier", 10))
com_text_label.pack()

but_1=ttk.Button(window,command=play)
but_1.configure(text="Start",bg="black",fg="red",padx=50)
but_1.pack()

but_2=ttk.Button(window,command=window.destroy)
but_2.configure(text="Exit",bg="black",fg="red",padx=50)
but_2.pack()

window.mainloop()