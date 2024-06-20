from translate import Translator
import pyperclip
lang = input("What language will you be translating from?: ")
while True:
    text = input("Text to translate:")
    translator= Translator(from_lang=lang, to_lang="zh")
    translation = translator.translate(text)    
    pyperclip.copy("say_team" + " " + translation)
