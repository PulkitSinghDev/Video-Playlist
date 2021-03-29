from moviepy.editor import *

video_list = [] 
#enter your videos here 

ah = video_list[0]
for i in video_list():
	clip=VideoFileClip(str(i.Video))
        allchunks.append(clip)

final_clip=concatenate_videoclips(allchunks)
final_clip.write_videofile(ah)
