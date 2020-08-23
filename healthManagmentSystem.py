
""" Health Management System """

def clientsInfo():
    print("Now you are Log the user's data:")
    Name = input("Please Enter The User Name:")
    if Name.lower() == "harry":
        print("Wellcome !", Name)
        harryRountine= input("What you want to log 'Exercise' press 'E' and for 'Diet' press 'D':")
        if harryRountine.lower() == "e":
            harryExercise = input("Enter your today's exercise:")
            harryE = f" Exercise date is: '{str(getdate())}'  Great you did : '{harryExercise}' exercises.Keep it up!!"
            # print("Todays Exercise: ", harryE)
            with open("harryNote.txt", "a") as f:
                f.write("\n" + str(harryE))
                print("Your Exercise Note is successfully written")
        elif harryRountine.lower() == "d":
            harryDiet = input("Enter your today's Diet:")
            harryD = f" Diet date: '{str(getdate())}' , You ate: '{harryDiet}' which is enough for today."
            # print("Todays Diet: ", harryD)
            with open("harryNote.txt", "a") as f:
                f.write("\n" + str(harryD))
                print("Your Diet Note is successfully written")

    elif Name.lower() == "rohan":
        print("Wellcome !", Name)
        rohanRountine = input("What you want to log 'Exercise' press 'E' and for 'Diet' press 'D':")
        if rohanRountine.lower() == "e":
            rohanExercise = input("Enter your today's exercise:")
            rohanE = f"Exercise date is: '{str(getdate())}' ,Great you did : '{rohanExercise}' exercises,Keep it up!!"
            # print("Todays Exercise: ", rohanE)
            with open("rohanNote.txt", "a") as f:
                f.write("\n" + str(rohanE))
                print("Your Exercise Note is successfully written")
        elif rohanRountine.lower() == "d":
            rohanDiet = input("Enter your today's Diet:")
            rohanD = f" Diet date: '{str(getdate())}' , You ate: '{rohanDiet}' which is enough for today."
            # print("Todays Diet: ", rohanD)
            with open("rohanNote.txt", "a") as f:
                f.write("\n" + str(rohanD))
                print("Your Diet Note is successfully written")

    elif Name.lower() == "hammad":
        print("Wellcome !", Name)
        hammadRountine = input("What you want to log 'Exercise' press 'E' and for 'Diet' press 'D':")
        if hammadRountine.lower() == "e":
            hammadExercise = input("Enter your today's exercise:")
            hammadE = f"Exercise date is: '{str(getdate())}' ,Great you did : '{hammadExercise}' exercises.Keep it up!!"
            # print("Todays Exercise: ", hammadE)
            with open("hammadNote.txt", "a") as f:
                 f.write("\n" + str(hammadE))
                 print("Your Exercise Note is successfully written")
        elif hammadRountine.lower() == "d":
            hammadDiet = input("Enter your today's Diet:")
            hammadD = f" Diet date: '{str(getdate())}' , You ate: '{hammadDiet}' which is enough for today."
            # print("Todays Diet: ", hammadD)
            with open("hammadNote.txt", "a") as f:
                f.write("\n" + str(hammadD))
                print("Your Diet Note is successfully written")
        else:
            print("Your entered invalid data")
            exit()
    else:
        print("Your enter incorrect client name, enter again:")
        clientsInfo()
    startProgram()
    return

def getdate():
    import time
    localTime = time.asctime(time.localtime(time.time()))
    return localTime

def clientdetails():
    print("Now you are Retrieve any user's data:")
    Name = input("Please Enter The User Name:")
    if Name.lower() == "harry":
        print("Wellcome !", Name)
        with open("harryNote.txt") as f:
            print(f.readlines())
    elif Name.lower() == "rohan":
        print("Wellcome !", Name)
        with open("rohanNote.txt") as f:
            print(f.readlines())
    elif Name.lower() == "hammad":
        print("Wellcome !", Name)
        with open("hammadNote.txt") as f:
            print(f.readlines())
    else:
        print("Your enter incorrect name, enter again:")
        clientdetails()
    startProgram()
    return

def startProgram():
    print("\nThere are three clients for now:  'Harry' , 'Rohan', 'Hammad': ")
    print("If you want to Log data press 'L' and for Retrieve data press 'R': ")
    data = input("Please Tell what you want 'L' or 'R':")
    if data.lower() == "l":
        clientsInfo()
    elif data.lower() == "r":
        clientdetails()
    else:
        print("Your are entered wrong data..try again")
        startProgram()
print(f"Wellcome to health care system {startProgram()}")
print(" Write clients Information: ", clientsInfo())
print("Read clients Information: ", clientdetails())