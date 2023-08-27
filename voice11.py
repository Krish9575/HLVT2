import speech_recognition as sr
from googletrans import Translator
from playsound import playsound
from gtts import gTTS
import os
import pyttsx3
from tkinter import *
from PIL import ImageTk

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 165)
translator = Translator()


class Voice_assistance:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')

        self.bg = ImageTk.PhotoImage(file="E:\\Code\\images\\background.png")
        Label(self.root, image=self.bg).place(x=0, y=0)

        self.centre = ImageTk.PhotoImage(file="E:\\Code\\images\\frame_image.jpg")
        Label(self.root, image=self.centre).place(x=50, y=350, width=490, height=280)

        # ====start button
        Button(self.root, text='START', font=("times new roman", 14), command=self.Voice_command).place(x=80, y=510)
        # ====close button
        Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window).place(x=425,y=510)

    def Voice_command(self):
        def speak(text):
            engine.say(text)
            engine.runAndWait()

        def take_command():
            r = sr.Recognizer()
            my_micro = sr.Microphone(device_index=1)
            try:
                with my_micro as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    r.pause_threshold = 1
                    audio = r.listen(source, timeout=1)
                    query = r.recognize_google(audio)
                    query = query.lower()
                    return query
            except:
                pass

        def trans(text, lang_input):
            translator_text = translator.translate(text, dest=lang_input)
            print(translator_text.text)
            speech = gTTS(text=translator_text.text, lang=lang_input, slow=False)
            speech.save('hindi.mp3')
            playsound('hindi.mp3')
            os.remove('hindi.mp3')

        speak(
            "hello there ,i am your assistance and my work is to translate human language into another language ")

        speak("please tell me in what language you want to translate")

        dict_Language = {
            'afrikaans': 'af',
            'albanian': 'sq',
            'amharic': 'am',
            'arabic': 'ar',
            'armenian': 'hy',
            'azerbaijani': 'az',
            'basque': 'eu',
            'belarusian': 'be',
            'bengali': 'bn',
            'bosnian': 'bs',
            'bulgarian': 'bg',
            'catalan': 'ca',
            'cebuano': 'ceb',
            'chichewa': 'ny',
            'chinese simple': 'zh-cn',
            'chinese traditional': 'zh-tw',
            'corsican': 'co',
            'croatian': 'hr',
            'czech': 'cs',
            'danish': 'da',
            'dutch': 'nl',
            'english': 'en',
            'esperanto': 'eo',
            'estonian': 'et',
            'filipino': 'tl',
            'finnish': 'fi',
            'french': 'fr',
            'frisian': 'fy',
            'galician': 'gl',
            'georgian': 'ka',
            'german': 'de',
            'greek': 'el',
            'gujarati': 'gu',
            'haitian creole': 'ht',
            'hausa': 'ha',
            'hawaiian': 'haw',
            'hebrewi': 'iw',
            'hebrew': 'he',
            'hindi': 'hi',
            'hmong': 'hmn',
            'hungarian': 'hu',
            'icelandic': 'is',
            'igbo': 'ig',
            'indonesian': 'id',
            'irish': 'ga',
            'italian': 'it',
            'japanese': 'ja',
            'javanese': 'jw',
            'kannada': 'kn',
            'kazakh': 'kk',
            'khmer': 'km',
            'korean': 'ko',
            'kurdish': 'ku',
            'kyrgyz': 'ky',
            'lao': 'lo',
            'latin': 'la',
            'latvian': 'lv',
            'lithuanian': 'lt',
            'luxembourgish': 'lb',
            'macedonian': 'mk',
            'malagasy': 'mg',
            'malay': 'ms',
            'malayalam': 'ml',
            'maltese': 'mt',
            'maori': 'mi',
            'marathi': 'mr',
            'mongolian': 'mn',
            'myanmar': 'my',
            'nepali': 'ne',
            'norwegian': 'no',
            'odia': 'or',
            'pashto': 'ps',
            'persian': 'fa',
            'polish': 'pl',
            'portuguese': 'pt',
            'punjabi': 'pa',
            'romanian': 'ro',
            'russian': 'ru',
            'samoan': 'sm',
            'scots gaelic': 'gd',
            'serbian': 'sr',
            'sesotho': 'st',
            'shona': 'sn',
            'sindhi': 'sd',
            'sinhala': 'si',
            'slovak': 'sk',
            'slovenian': 'sl',
            'somali': 'so',
            'spanish': 'es',
            'sundanese': 'su',
            'swahili': 'sw',
            'swedish': 'sv',
            'tajik': 'tg',
            'tamil': 'ta',
            'telugu': 'te',
            'thai': 'th',
            'tr': 'turkish',
            'ukrainian': 'uk',
            'urdu': 'ur',
            'uyghur': 'ug',
            'uzbek': 'uz',
            'vietnamese': 'vi',
            'welsh': 'cy',
            'xhosa': 'xh',
            'yiddish': 'yi',
            'yoruba': 'yo',
        }
        check = True
        while check:
            Lang = take_command()
            try:
                lan = dict_Language[Lang]
                check=False
            except:
                speak("please say it again its not clear ")
                check=True



        speak("ready to translate please give input")
        while True:
            tex_audio = take_command()
            if tex_audio == 'exit command':
                break
            else:
                trans(str(tex_audio), str(lan))

    def close_window(self):
        self.root.destroy()


# ==== create tkinter window
root = Tk()

# === creating object for class
obj = Voice_assistance(root)

# ==== start the gui
root.mainloop()
