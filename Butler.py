import wolframalpha
import speech_recognition as sr
import pyttsx3 as py
import webbrowser

r = sr.Recogniser()
client = wolframalpha.client('8LAJL7-7AJ83URGJ5')
mic = sr.Microphone()
engine = py.init()

with mic as source:
    audio = r.listen(source)
    recognised_text = sr.recognise_google(audio)
    print(recognised_text)
    query = str(recognised_text)
    res = client.query(query)
    output = next(res.results).text
    print(output)
    engine.say(output)
    webbrowser.open(output)
    engine.runAndWait()
