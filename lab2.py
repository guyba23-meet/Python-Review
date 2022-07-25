def create_youtube_video (title, description):
	vidDict = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
	return vidDict
def like (vidDict):
	if "likes" in vidDict:
		vidDict["likes"]+=1
	return vidDict
def dislike (vidDict):
	if "dislikes" in vidDict:
		vidDict["dislikes"]+=1
	return vidDict
def add_comment (vidDict, username, comment_text):
	vidDict["comments"][username] = comment_text
	return vidDict
title = input("Enter vid title")
description = input("Enter vid description")
video = create_youtube_video(title,description)
for i in range(542):
	like(video)


dislike(video)
add_comment(video, "Guy", "Cool!")
print (video)