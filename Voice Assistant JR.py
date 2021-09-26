#!/usr/bin/env python
# coding: utf-8

# In[3]:



import pyttsx3 #Speak something
import speech_recognition as sr #Recognize audio and writte
import webbrowser
import datetime #dates
import pywhatkit
import os 
import yfinance as yf
import pyjokes
import pyaudio #Hear what i say
import wikipedia #Wikipedia


# In[3]:


#listen to our microphone and return the audio as text using google
def transform():
    r = sr.Recognizer()
    with sr.Microphone() as source: #Listen what you say
        r.pause_threshold = 0.8
        said = r.listen(source)
        try:
            print('I am listenning')
            q = r.recognize_google(said, language="en") 
            return q
        except sr.UnknownValueError:
            print("Sorry i dont understand")
            return "I am waiting"
        except sr.RequestError:
            print('Sorry the service is down')
            return "I am waiting"
        except:
            return "I am waiting"


# In[4]:


transform()


# In[5]:


def speaking(message):
    engine = pyttsx3.init() #Take text and return audio
    engine.say(message)
    engine.runAndWait()


# In[6]:


speaking('Hello world')


# In[7]:


engine = pyttsx3.init()
for voice in engine.getProperty('voices'):
    print(voice)


# In[8]:


id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice',id)
engine.say('Hello world')
engine.runAndWait()


# In[1]:


#Return the weekday name
def query_day():
    day=datetime.date.today()
    #print(day)
    weekday=day.weekday()
    #print(weekday)
    mapping = {
        0:'Monday',1:'Tuesday',2:'Wendsday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'
    }
    try:
        speaking(f'Today is {mapping[weekday]}')
    except:
        pass


# In[2]:


query_day()


# In[11]:


#Returns the time
def query_time():
    time=datetime.datetime.now().strftime('%I:%M')
    speaking(f"{time[0:2]}o'clock and {time[3:5]}minutes")
    


# In[12]:


query_time()


# In[13]:


#Intro greeting at startup
def whatsup():
    speaking('''Hi, I am JR. Your voice assistant
    How may i help you
    ''')


# In[14]:


whatsup()


# In[31]:


#The heart od my Assistant.Takes queries and returns answers
def querying():
    whatsup()
    start = True
    while(start):
        q = transform().lower()
        
        if'open youtube' in q:
            speaking('Starting youtube for you. Just a second')
            webbrowser.open('https://www.youtube.com')
            continue
            
        elif 'open google' in q:
            speaking('Opening google')
            webbrowser.open('https://www.google.com/')
            continue
        
        elif 'open netflix' in q:
            speaking('Starting netflix for you. Just a second')
            webbrowser.open ('https://www.netflix.com/mx')
            continue
            
        elif 'open spotify' in q:
            speaking('starting spotify, wait')
            webbrowser.open('https://open.spotify.com/?_gl=1*ox2ufe*_gcl_aw*R0NMLjE2MjkzOTUzMTcuQ2p3S0NBandndmlJQmhCa0Vpd0ExMEQyajVobnB1OGRzVl9QMUIwRG1ueFZUU2VQRVE2VEk4T2NtbHdoclc5dWR5SUZRQVUzN1Z2cUlCb0NjSXdRQXZEX0J3RQ..*_gcl_dc*R0NMLjE2MjkzOTUzMTcuQ2p3S0NBandndmlJQmhCa0Vpd0ExMEQyajVobnB1OGRzVl9QMUIwRG1ueFZUU2VQRVE2VEk4T2NtbHdoclc5dWR5SUZRQVUzN1Z2cUlCb0NjSXdRQXZEX0J3RQ..&_ga=2.100397982.1655694793.1632499707-271096109.1629395317')
            continue
            
        elif 'open classroom' in q:
            speaking('Opening classroom, wait')
            webbrowser.open('https://classroom.google.com')
            continue
        
        elif 'open gmail' in q:
            speaking('Opening your mails, wait')
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            continue
            
        elif 'open scholar gmail' in q:
            speaking('Opening scholar mail')
            webbrowser.open('https://mail.google.com/mail/u/1/#inbox')
            continue
            
        elif 'open whatsapp' in q:
            speaking('Opening whatsapp')
            webbrowser.open('https://web.whatsapp.com')
            continue
            
        elif 'what day is it' in q:
            query_day()
            continue
            
        elif 'what time is it' in q:
            query_time()
            continue
            
        elif 'stop' in q:
            speaking('Have a Good day JR')
            break
            
        elif 'from wikipedia' in q:
            speaking('checking wikipedia')
            q =q.replace("wikipedia","")
            result = wikipedia.summary(q,sentences=2)
            speaking('found on wikipedia')
            speaking(result)
            continue
            
        elif 'your name' in q:
            speaking('I am JR, your voice assistant')
            continue
                     
        elif 'search.web' in q:
            pywhatkit.serach(q)
            speaking('That is what i found')
            continue
                     
        elif 'play' in q:
            speaking(f'playing{q}')
            pywhatkit.playonyt(q)
            continue
                     
        elif 'joke' in q:
            speaking(pyjokes.get_joke())
            continue
                     
        elif 'stock price' in q:
            search = q.split('of')[-1].strip()
            lookup = {'apple':'AAPL',
                     'amazon':'AMZN',
                     'google':'GOOGL'}
            try:
                stock = lookup[search]
                stock=yf.Ticker(stock)
                currentprice = stock.info['regularMarketPrice']
                speaking(f'found it, the price for {search}is {currentprice}')
                continue
            except:
                speaking(f'sorry i have no data for {search}')
                continue
                


# In[32]:


querying()


# In[ ]:





# In[ ]:




