from gtts import gTTS

def speakeng(text, language):
    tts = gTTS(text, lang=language)
    tts.save('media/speecheng.mp3')

def speakhi(text, language):
    tts = gTTS(text, lang=language)
    tts.save('media/speechhi.mp3')

def speakmr(text, language):
    tts = gTTS(text, lang=language)
    tts.save('media/speechmr.mp3')

# text_to_speak = input("What do you want to say: ")
# speak(text_to_speak, "en")
