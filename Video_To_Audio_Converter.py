from email.mime import audio
import moviepy.editor
video=moviepy.editor.VideoFileClip("C:/Users/Akshay/Desktop/game.mp4")
audio=video.audio
audio.write_audiofile("C:/Users/Akshay/Desktop/g.mp3")