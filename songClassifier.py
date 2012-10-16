#!/usr/bin/python
import os
import fnmatch
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import shutil

print "\t***Welcome To Song Classifier****"
sourceDir = raw_input("Enter Absolute path of songs source directory: ")
destDir = raw_input("Enter absolute path of songs destination directory: ")
#checking correctness of path
pathCheck = sourceDir[len(sourceDir)-1]
if(pathCheck != '/'):
	sourceDir = sourceDir + '/'

pathCheck = destDir[len(destDir)-1]
if(pathCheck != '/'):
	destDir = destDir + '/'

yDir=destDir+"yearwise/"
aDir=destDir+"artists/"
try:
	os.mkdir(destDir)
	os.mkdir(yDir)
	os.mkdir(aDir)
except  OSError:
	pass

print "[INFO] Classifying..."
#function defination
def find_mp3(filetype,source):
   for path, dirlist, filelist in os.walk(source):
      for name in fnmatch.filter(filelist,filetype):
          yield os.path.join(path,name)

listSongs=find_mp3("*.mp3",sourceDir)
for song in listSongs:
	data = MP3(song,ID3=EasyID3).values
	fields=data() 			
	length=len(fields)
	
	year="Unlisted Year"
	artist="Unlisted Artist"
	
	if length==1:
		year=fields[0]
	if length >1:
		year=fields[0]
		artist=fields[1]

	
	yearDir=yDir+year[0]+'/'
	artistDir=aDir+artist[0]+'/'
	
	try:
		os.mkdir(yearDir)
		os.mkdir(artistDir)
	except  OSError:
		pass
	
	try:
		shutil.copy(song,yearDir)
		shutil.copy(song,artistDir)
	except	IOError:
		pass
	
print "[INFO] Successfully Classified Please check folder :" +destDir

