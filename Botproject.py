import os
import pyttsx3
import speech_recognition as SRG
import smtplib
from twilio.rest import Client


pyttsx3.speak("I am Aadarsh I am service provider which service you want from me tell please. ")

print("I can open Notepad for you")
pyttsx3.speak("I can open Notepad for you")
print("I can open google chrome for you")
pyttsx3.speak("I can open google chrome for you")
print("I can open VLC media player for you")
pyttsx3.speak("I can open VLC media player for you")
print("I can send mail for you")
pyttsx3.speak("I can send mail for you")
print("I can send whatsapp msg for you")
pyttsx3.speak("I can send whatsapp msg for you")
print("I can open Faebook for you")
pyttsx3.speak("I can open Faebook for you")
print("I can open Instagram for you")
pyttsx3.speak("I can open Instagram for you")
print("I can open Linkdin for you")
pyttsx3.speak("I can open Linkdin for you")
print("I can open Calculator for you")
pyttsx3.speak("I can open Calculator for you")
print("I can open Youtube for you")
pyttsx3.speak("I can open Youtube for you")
print("I can play song for you")
pyttsx3.speak("I can play song for you")
print('I can open media player for you')
pyttsx3.speak('I can open media player for you')
print('Which Service you want from me')
pyttsx3.speak('Which Service you want from me')

while True:
    variable = SRG.Recognizer()
    with SRG.Microphone() as source:
        print('How may I help you?')
        engine.runAndWait()
        
        audio_input = variable.record(source,duration=6)
        try:
            n = variable.recognize_google(audio_input)
            n = n.lower()
            print(n)
        except:
            print('Could not process audio...')
            pyttsx3.speak('Could not process audio')
            break
    
    
    if((('text' in n) or ('editor' in n) or ('notepad' in n)) and (('run' in n) or ('open' in n))):
        pyttsx3.speak("your Notepad is opening")
        print(os.system('Notepad'))
        

    elif(('chrome' in n or 'google' in n or 'web' in n or 'browser' in n) and ('run' in n or 'open' in n)):
        pyttsx3.speak("your chrome is running")
        print(os.system('Chrome'))

    elif(('vlc' in n or 'media' in n or 'player' in n or 'music' in n) and ('play' in n or 'open' in n or 'run' in n)):
        pyttsx3.speak("VLC is opening")
        print(os.system('vlc'))

    elif(('mail' in n or 'email' in n) and ('send' in n)):
        content = input('what message you want to send type here: ' ) #465
        mail = smtplib.SMTP_SSL('smtp.gmail.com',465)
        print("""Go in this site and ON the less secure app access for sending the message https://support.google.com/accounts/answer/6010255 after send
              the messsage please turn back off this.""")
        email = input('enter email: ')
        password = input('enter password: ')
        mail.login(email,password)
        reciver = input('enter reciever gmail id: ')
        mail.sendmail(email,reciver,content)
        mail.quit()
        pyttsx3.speak("Mail sent")
        
    elif('send' in n and 'msg' in n and 'whatsapp'):
        auth = input()
        token = input()
        client = Client(auth,token)
        from_whatsapp_number = 'whatsapp:+919536493871'
        to_whatsapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER'] 
        client.messages.create(body='aadarsh tiwari!',from_= from_whatsapp_number,to = to_whatsapp_number)
        pyttsx3.speak("msg sent")

    elif (('open' in n) or ('run' in n)) and ('linkedin' in n):
        pyttsx3.speak('Opening Linkedin')
        os.system('chrome https://www.linkedin.com/feed/')

    elif (('open' in n) or ('run' in n)) and (('facebook' in n)):
        pyttsx3.speak('Opening Facebook')
        os.system('chrome https://www.facebook.com/')

    elif (('open' in n) or ('run' in n)) and ('youtube' in n):
        pyttsx3.speak('Opening Youtube')
        os.system('chrome https://www.youtube.com/')

    elif ('play' in n) and ('song' in n):
        pyttsx3.speak('Playing Song')
        os.system('chrome https://gaana.com/playlist/sksujauddin2ganacomsongs')

    elif (("open" in n) or ('run' in n)) and ("player" in n) and ("media" in n):
        pyttsx3.speak('Opening media player')
        os.system('wmplayer')

    elif (("open" in n) or  ("execute" in n)) and (("calculator" in n)):
        pyttsx3.speak('Opening calculator')
        os.system('calc')

    elif (('open' in n) or ('run' in n)) and (('instagram' in n)):
        pyttsx3.speak('Opening Instagram')
        os.system('chrome https://www.instagram.com')

    elif(n == 'exit' or n=='quit' or n == 'outside'):
        pyttsx3.speak("Thanks for coming Thank you.")
        print("Thanks for coming Thank you.")
        break  
        
    else:
        pyttsx3.speak("This operation is not support we are glad to help you please enter your next operation what you want to perform: ")
        print('This operation is not support we are glad to help you please enter your next operation what you want to perform: ')
        
    

