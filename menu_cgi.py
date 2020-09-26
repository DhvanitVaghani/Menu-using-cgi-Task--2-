import webbrowser as wb
import speech_recognition as sr
import pyttsx3 as pysp

r = sr.Recognizer()

print('Welcome to my menu using cgi program')
print('Menu:')  
print('Can you show date')
print('hey, please show me calendar')
print('Hey please launced one os for me')

with sr.Microphone() as source:
    pysp.speak("Hey Tell me what do you want")
    print("Tell me what do you want....",end='')
    audio = r.listen(source)
x=r.recognize_google(audio)

if 'date' in x:
    wb.Chrome('chrome').open('http://192.168.56.101/cgi-bin/menu.py?c=date')    
elif 'cal' in x:
    wb.Chrome('chrome').open('http://192.168.56.101/cgi-bin/menu.py?c=cal')
elif 'os' in x or 'operating system' in x:
    pysp.speak('Yes,sure')
    print('Enter osname:',end='')
    os_name = input()
    print('1. ubuntu:18.04')
    print('2. centos:latest')
    print('Select index 1 or 2:',end='') 
    os_image=input()
    if os_image=='1':
        wb.Chrome('chrome').open('http://192.168.56.101/cgi-bin/dockerrun.py?o={0}&i=ubuntu%3A18.04'.format(os_name))
    elif os_image=='2':
        wb.Chrome('chrome').open('http://192.168.56.101/cgi-bin/dockerrun.py?o={0}&i=centos%3Alatest'.format(os_name))
else:
    print("I can't understand!")            
