print("Welcome to my Computer Quiz!")

playing = input("Do  you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print('Correct! :> ')
    score += 1
else:
    print('Incorrect! :( ')

answer = input("What does GPU stand for? ")
if answer == "Graphics Processing Unit":
    print('Correct! :> ')
    score += 1
else:
    print('Incorrect! :( ')

answer = input("What does RAM stand for? ")
if answer == "Random Access Memory":
    print('Correct! :> ')
    score += 1
else:
    print('Incorrect! :( ')

answer = input("What does PSU stand for? ")
if answer == "Power Supply":
    print('Correct! :> ')
    score += 1
else:
    print('Incorrect! :( ')

answer = input("What's my Name? ")
if answer == "Gelo Pogi":
    print('Correct! :> ')
    score += 1
else:
    print('Incorrect! :( ')

print("You got " + str(score) + " Questions Correct!")
print("You got " + str((score /5 ) * 100) + "%. ")


 

