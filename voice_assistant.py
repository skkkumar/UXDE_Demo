import speech_recognition
from gtts import gTTS
import playsound
import os
import sys
import webbrowser
import secrets


def assistant_voice(command):
    print("Avatar: " + command)
    avatar_voice = gTTS(text=command, lang='en', slow=False)

    file = str("temp_sound_file") + ".mp3"
    avatar_voice.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)
    return


def listen_to_command():
    recognizer = speech_recognition.Recognizer()
    audio = ''

    with speech_recognition.Microphone() as source:
        print('Say something...')
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said: ", text)
        return text
    except speech_recognition.UnknownValueError:
        assistant_voice("Sorry, I could not understand your command.")
        command = listen_to_command()
    return command


def voice_assistant(command):
    happy_songs = ["https://www.youtube.com/watch?v=3ssL8vx7Xhg&list=PLIILL6veL7802G94eulr2fzj0wz7CwKqh",
                   "https://www.youtube.com/watch?v=C5oBuAyocsA&list=PLIILL6veL7802G94eulr2fzj0wz7CwKqh&index=2",
                    "https://www.youtube.com/watch?v=W1xwTqgzQ_g&list=PLIILL6veL7802G94eulr2fzj0wz7CwKqh&index=3"]
    metal_songs = ["https://www.youtube.com/watch?v=xnKhsTXoKCI&list=PLhQCJTkrHOwSX8LUnIMgaTq3chP1tiTut",
                   "https://www.youtube.com/watch?v=J51LPlP-s9o&list=PLhQCJTkrHOwSX8LUnIMgaTq3chP1tiTut&index=2",
                   "https://www.youtube.com/watch?v=KV5ffXxFI38"]
    if "play music" in command:
        assistant_voice("metal or upbeat?")
        genre = listen_to_command()
        if "metal" in genre:
            webbrowser.open(secrets.choice(metal_songs))
        elif "upbeat" in genre:
            webbrowser.open(secrets.choice(happy_songs))
    elif 'shut down' in command:
        assistant_voice('I am shutting down. Have a nice day. ')
        sys.exit()
    return

assistant_voice('Hi User, I am Avatar, your personal voice assistant. Please give me a command to get started.')
# loop to continue executing multiple commands
while True:
    voice_assistant(listen_to_command())