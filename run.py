import os
import argparse
from moviepy.editor import VideoFileClip
import shutil
from subprocess import call

in_path = 'image'
out_path = 'video'

# def dir_path(string):
#     if os.path.isdir(string):
#         return string
#     else:
#         raise NotADirectoryError(string)

# parser = argparse.ArgumentParser()
# parser.add_argument(type=dir_path)

def make_gif(filepath):
	print(filepath)
	out_folder = os.path.split(filepath)[0]
	filename = os.path.splitext(os.path.basename(filepath))[0]

	shutil.copy(filepath, in_path)
	video = os.path.join(out_path, filename+'_.mp4')

	call(['python3', 'main.py'])
	call("ffmpeg -y -ss 00:00:00 -t 2 -i " + os.path.join(out_path, filename+'_.mp4') + " -filter_complex \"[0:v] palettegen\" palette.png", shell=True)
	call("ffmpeg -y -ss 00:00:00 -t 2 -i " + os.path.join(out_path, filename+'_.mp4') + " -i palette.png -filter_complex \"[0:v] fps=10,scale=720:-1 [new];[new][1:v] paletteuse\" " + os.path.join(out_folder, filename+'.gif'), shell=True)
	os.remove(os.path.join(in_path, filename+'.jpeg'))
	os.remove(os.path.join('BoostingMonocularDepth/inputs', filename+'.jpeg'))


parser = argparse.ArgumentParser()
in_filepath = parser.parse_known_args()
in_filepath = in_filepath[1][0]

if os.path.isdir(in_filepath) and len(os.listdir(in_filepath)) != 0:
	for file in os.listdir(in_filepath):
		filepath = os.path.join(in_filepath, file)
		make_gif(filepath)
elif os.path.isfile(in_filepath):
	make_gif(in_filepath)
else:
	raiseError('Not a file or dir is empty')
make_gif(in_filepath)