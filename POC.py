import os
import cv2
import youtube_dl

saved_url = "https://youtu.be/UvFXPLWTPFQ"

url=saved_url #The Youtube URL
ydl_opts={}
ydl=youtube_dl.YoutubeDL(ydl_opts)
info_dict=ydl.extract_info(saved_url, download=False)

formats = info_dict.get('formats',None)
print("Obtaining frames")
for f in formats:
	if f.get('format_note',None) == '144p':
		url = f.get('url',None)
		cap = cv2.VideoCapture(url)
		x=0
		count=0
		while x<10:
			ret, frame = cap.read()
			if not ret:        
				print("Can't receive frame (stream end?). Exiting ...")
				break
			filename =r"D:\test\shot"+str(x)+".png"
			print(filename)
			x+=1
			cv2.imshow('frame', frame)
			cv2.imwrite(filename.format(count), frame)
			count+=300 #Skip 300 frames i.e. 10 seconds for 30 fps
			cap.set(1,count)
			if cv2.waitKey(30)&0xFF == ord('q'):
				break
		cap.release()