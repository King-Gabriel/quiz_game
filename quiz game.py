print("Welcome to my quiz game!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    print("You ain't playing :(")
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("? ")
if answer.lower() == "":
     print("Correct!")
     score += 1
else:
    print("Incorrect!")

answer = input("? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("? ")
if answer.lower() == "":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")



