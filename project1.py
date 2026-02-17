story_num = input("Type number: ")
if not story_num.isdigit:
    print("Invalid number")
    input("another number: ")

if(story_num == "1"):
    arr = ["Input a number: ", "Input a measure of time","Input Mode of Transportation", "Input an adjective: ", "Input an adjective: ", "Input a noun: ", "Input a color: ", "Input a body part: ", "Input a verb: ", "Input a number: ", "Input a noun: ", "Input a noun: ", "Input a body part: ", "Input a verb: ", "Input a noun: ", "Input an adjective: ", "Input a silly word: ", "Input a noun: "]
    
    for i in range(len(arr)):
        arr[i] = input(arr[i])
        arr[i] = arr[i].strip()
    print("It was about " + arr[0] + " ago when I arrived at the hospital in a  " + arr[1] + ". The hospital is a/an " + arr[2] + " place, there are a lot of " + arr[3] + " " + arr[4] + " here. There are nurses here who have  " + arr[5] + " " + arr[6] + ". If someone wants to come into my room I told them that they have to " + arr[7] + "   first. I’ve decorated my room with (" + arr[8] + " " + arr[9] + "). Today I talked to a doctor and they were wearing a " + arr[10] + " on their " + arr[11] + ". I heard that all doctors  " + arr[12] +"    "+ arr[13] +"  every day for breakfast. The most "+ arr[14] +"  thing about being in the hospital is the "+ arr[15] +" "+ arr[16] +" !")
elif(story_num == "2"):
    arr = ["Input the person's name: ", "Input a noun: ", "Input an adjective(feeling): ", "Input a verb: ", "Input an adjective(feeling): ", "Input an animal: ", "Input a verb: ", "Input a color: ", "Input a verb(-ing form): ", "Input an adverb(-ly form): ", "Input a number: ", "Input a measure of time","Input a color: ", "Input an animal: ", "Input a number: ", "Input a silly word: ", "Input a noun: "]
    for i in range(len(arr)):
        arr[i] = input(arr[i])
        arr[i] = arr[i].strip()
    print("This weekend I am going camping with " + arr[0] + " . I packed my lantern, sleeping bag, and  " + arr[1] + " . I am so " + arr[2] + "to" + arr[3] + " in a tent. I am  " + arr[4] + " we might see a(n) " + arr[5] + " , I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and " + arr[6] + " . I have heard that the " + arr[7] + " lake is great for" + arr[8] +" . Then we will " + arr[9] + " hike through the forest for " + arr[10] + " "+arr[11]+ " . If I see a " + arr[12] + " "+arr[13]+" while hiking, I am going to bring it home as a pet! At night we will tell  " + arr[14] + " " +arr[15]+" stories and roast " + arr[16] + " around the campfire!!")
elif(story_num== "3"):
    arr = ["Input the person's name: ","Input an adjective: ", "Input a color: ", "Input an animal: ", "Input a place name: ", "Input an adjective: ", "Input a megical creature(plural): ","Input an anjective: ", "Input a megical creature(plural): ", "Input a room name in a house: ", "Input a noun: ","Input a noun: ", "Input a noun(prular): ", "Input an adjective: ", "Input a noun(plural): ", "input a number: ","Input a meausre of time: ", "Input a verb(-ing form): ", "Input an adjective: ", "Input a noun: "]
    for i in range(len(arr)):
        arr[i] = input(arr[i])
        arr[i] = arr[i].strip()
    print("Dear "+arr[0]+" , I am writing to you from a  "+arr[1]+"  castle in an enchanted forest. I found myself here one day after going for a ride on a  "+arr[2]+"   "+arr[3]+" in  "+arr[4]+" . There are  "+arr[5]+"  "+arr[6]+"  and  "+arr[7]+"  "+arr[8]+"  here! In the  "+arr[9]+"  there is a pool full of  "+arr[10]+" . I fall asleep each night on a  "+arr[11]+"  of "+arr[12]+"  and dream of  "+arr[13]+"   "+arr[14]+" . It feels as though I have lived here for  "+arr[15]+"  "+arr[16]+" . I hope one day you can visit, although the only way to get here now is  "+arr[17]+"  on a  "+arr[18]+"  "+arr[19]+" !!")



