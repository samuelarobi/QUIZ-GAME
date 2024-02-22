print("Hello")
print("Welcome To My Computer Quiz")
Playing = input("Do You Want To Play? ")
if playing != "Yes":
    quit()
print("Okay! Let's Play:")
score=0
answer = input("What Does CPU Stand For? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("incorrect!")
answer = input("What Does GPU Stand For? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("incorrect!")
answer = input("What Does Ram Stand For? ")
if answer.lower() == "random acess memory":
    print("Correct!")
    score+=1
else:
    print("incorrect!")
answer = input("What Does PSU Stand For? ")
if answer.lower()== "power supply":
    print("Correct!")
    score+=1
else:
    print("incorrect!")
answer = input("What Does HR Stand For? ").lower()
if answer== "human resources":
    print("Correct!")
    score+=1 
else:
    print("incorrect!")
print("You got"+str(score)+"Question Correct!")
print("You got"+str((score/5)*100) +"%.")
