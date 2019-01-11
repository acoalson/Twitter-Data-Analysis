import pickle
import datetime
from datetime import datetime
fileName = input("Name of a file containing twitter data: ")
file = open(fileName,'rb')
data = pickle.load(file) #The list (with 21 objects)
#Each object is a dictionary with 25,26,27 elements

#-------------How many tweets are contained in the file?-------------
print("There are " + str(len(data)) + " tweets in the file")



#--------What are the earliest and latest date/time for the tweets in the file?------
#Look for the 'created_at' key
stringDates = list()
for element in data:
      stringDates.append(element['created_at'])

dates = list()
for x in stringDates:     #Formats dates into readable datetime format
      formatted = datetime.strptime(x, '%a %b %d %H:%M:%S %z %Y')
      dates.append(formatted)
    
minD = min(dates)
maxD = max(dates)

#Changes the time to my time zone PDT
print("Earliest date/time: "+minD.strftime('%c'))
print("Latest date/time: "+maxD.strftime('%c'))



#What are the 3 most common hashtags in the set of tweets and their number of instances?
#------If there are ties, be sure to include each of the "tied" hashtags-------------
#Look for the 'entities key'

hashCount = dict()
for h in data:
    hashList=h['entities']['hashtags']
    if len(hashList)!=0: #there are hashtags
        for hashDict in hashList:
            tag=hashDict['text']
            if tag in hashCount:
                hashCount[tag]+=1
            else:
                hashCount[tag]=1

print("Most frequent hashtags")
sortedHashC = sorted(hashCount.items(), key = lambda tuple: tuple[1], reverse=True) #Formats the dictionary and reverse sorted it by dict value
place=1
lastCount=sortedHashC[0][1]
for i in sortedHashC:
    if i[1]!=lastCount:
        place+=1
    if place<=3:
        print("  #"+str(place)+" Tag="+i[0]+" / Count="+str(i[1]))
    lastCount=i[1]


#select a tweet, and select a field, and print out the data that the user selected.

fieldOptions = [
        'created_at',
        'favorite_count',
        'filter_level',
        'name',
        'screen_name',
        'truncated',
        'source',
        'text',
        'contributors',
        'retweet_count'
        ]
repeat = True   
while repeat:
    tweetNum=0
    while not(tweetNum>=1 and tweetNum<=len(data)): #error checking. Assumes passed in an int
        tweetNum=int(input("Input a tweet number from 1 to "+str(len(data))+": "))
    tweetNum-=1
    print("Type the number corresponding to the field you want to choose")
    print("1:Created At\n2:FavoriteCount\n3:Filter Level\n4:User name\n5:User Screen Name\n6:Truncated\n7:Source\n8:Text\n9:Contributors\n10:RetweetCount")
    fieldInp=0
    while not(fieldInp>=1 and fieldInp<=10): #error checking. Assumes passed in an int
        fieldInp=int(input("Field choice 1-10: "))
    field=fieldOptions[fieldInp-1]
    if field!='screen_name' and field!='name':
        print(field+": "+str(data[tweetNum][field]))
    else:
        print(field+": "+str(data[tweetNum]['user'][field]))
    r=input("Do you want to do this again? Type yes or no: ")
    if r=='no' or r=='No':
        repeat=False
