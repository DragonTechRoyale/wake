from datetime import *
import time 
import os
import random
import playsound
from py_console import console
from pathlib import Path


__PROGRAM_EXIT = "Exiting program..."


def main():
	music_path = str(Path(__file__).parent.resolve())  + "/music"
	wake_hour = "05"
	wake_minute = "00"
	temp = str(input("Enter wake hour in the two number format (ex: 05 for 5AM) or press enter for default hour (5AM): "))
	if temp != '':
		wake_hour = temp
  
	temp = str(input("Enter wake minute in the two number format (ex: 05 for 5 minutes) or press enter for default minute (00): "))
	if temp != '':
		wake_minute = temp

	temp = str(input("Specify the path of the folder with the music files) or press enter for default path (./music): "))
	if  temp != '':
		music_path = temp
		print("1")
  
	if (music_path[0] == '~'):
		music_path = music_path[:0] + os.path.expanduser('~') + music_path[1:]
	console.info(f"Printing files in {music_path}")
 
	try:
		files = []
		for file in os.listdir(music_path):
			print(file)
			files.append(file)
		if len(files) == 0 or (len(files) == 1 and files[0]=='.DS_Store'):
			console.error(f"music folder is probably empty, please add music files.\n{__PROGRAM_EXIT}")
			return
	except FileNotFoundError:
		os.mkdir(music_path)
		console.error(f"Default music folder does not exist, created one on the script's directory, please add music files.\n{__PROGRAM_EXIT}")
		return 
		
	while True:
		time.sleep(1)
		now = datetime.now()
		if str(now.hour) == wake_hour and str(now.minute) == wake_minute: 
			file = random.choice(os.listdir(music_path))
			while file[-1] != 'a' or file[-2] != '4' or file[-3] != 'm':
				file = random.choice(os.listdir(music_path))
			file = r'{}'.format(file)
			path_file = f"{music_path}/{file}"
			console.success(f"Playing: {path_file}")
			playsound.playsound(path_file, True)
   

if __name__ == '__main__':
	main()
