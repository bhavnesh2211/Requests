import os,json,requests,shutil
def file_checker():
	if os.path.isfile("all_cources_of_saral"):
		print "Already Exists. "
	else:
		print "Don't Exists."
		url = requests.get("http://saral.navgurukul.org/api/courses")
		with open("all_cources_of_saral.json","w") as file:
			json.dump(url.text,file)
# file_checker()

def name():
	with open("all_cources_of_saral.json","r") as data:
		read = data.read()
		load = json.loads(read)
		loads = json.loads(load)
		courses = loads["availableCourses"]
		for i in range (len(courses)):
			print str(courses[i]["name"])
 
def id_and_name():
	with open("all_cources_of_saral.json","r") as data:
		read = data.read()
		load = json.loads(read)
		loads = json.loads(load)
		courses = loads["availableCourses"]
		all_cources = {}
		for i in range (len(courses)):
			all_cources[courses[i]["id"]]= str(courses[i]["name"])
		print all_cources
		user = int(raw_input("Enter your cource id "))
		print all_cources[user]

def api_again():
	with open("all_cources_of_saral.json","r") as data:
		read = data.read()
		load = json.loads(read)
		loads = json.loads(load)
		courses = loads["availableCourses"]
		all_cources = {}
		for i in range (len(courses)):
			all_cources[courses[i]["id"]]= str(courses[i]["name"])
		return all_cources

def api_again1():
	data  = api_again()
	print data
	user = int(raw_input("Enter your cource id "))
	print data[user]
	copy_url = requests.get("http://saral.navgurukul.org/api/courses/%s/exercises" %user).text
	load = json.loads(copy_url)
	data1=load["data"]
	for i in data1:
		print "-------------%s-----------" %i["name"]
		if len(i["childExercises"]) > 0:
			childExercises= i["childExercises"]
			for j in childExercises:
				print j["name"]

data = api_again()
print data
user = input("Enter any id: ")
print data[user]
if os.path.exists(data[user]):
	shutil.rmtree(data[user])
os.mkdir(data[user])
def slug(user):
	copy_url = requests.get("http://saral.navgurukul.org/api/courses/%s/exercises" %user).text
	load = json.loads(copy_url)
	data1=load["data"]
	for i in data1:
		childExercises= i["childExercises"]
		slugName = ""
		slug = i["slug"]
		for j in slug:
			if j =="/":
				slugName+="_"
				continue
			slugName += j
		file_slug = open(data[user]+"//"+slugName+".txt", "w")
		url = requests.get("http://saral.navgurukul.org/api/courses/" + str(user) +"/exercise/getBySlug?slug=%s"%slug).text
		load = json.loads(url)
		file_slug.write(str(load))
		# json.dump(file_slug,)
slug(user)