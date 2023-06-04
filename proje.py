from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
import os
import imageio
from moviepy import editor

audio_path = os.path.join(os.getcwd(), ""mix_93m35s (audio-joiner.com).mp3"")

images_path = os.path.join(os.getcwd(), "2.png")

audio = MP3(audio_path)
# To get the total duration in milliseconds
audio_length = audio.info.length
  
# Get all images from the folder
# Create a list to store all the images
list_of_images = []
for image_file in os.listdir(images_path):
    if image_file.endswith('.png') or image_file.endswith('.jpg'):
     image_path = os.path.join(images_path, image_file)
    image = Image.open(image_path).resize
((400, 400), Image.ANTIALIAS)
list_of_images.append(image)

duration = audio_length/len(list_of_images)
imageio.mimsave('images.gif', list_of_images, fps=1/duration)