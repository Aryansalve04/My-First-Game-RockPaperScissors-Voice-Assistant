import random
import pyttsx3

computer=random.choice([1,2,3])

userinput=input("Enter your choice: ")
gamedict={"rock":1,"paper":2,"scissor":3,"r":1,"p":2,"s":3}
computerdict={1:"Rock",2:"Paper",3:"Scissor"}
user=gamedict[userinput]

bot=computerdict[computer]
you=computerdict[user]

print(f"\nLet's begin\n\nComputer choose: {bot}\nYou choose: {you}\n")
pyttsx3.speak(f"\nLet's begin\n\nComputer choose: {bot}\nYou choose: {you}\n")

if user==computer:
    print("The match results in a Draw!!!")
    pyttsx3.speak("The match results in a Draw!!!")
else:
    if user==2 and computer==3:
        print("Computer win")
        pyttsx3.speak("Computer WIN")
    elif user==1 and computer==2:
        print("Computer win")
        pyttsx3.speak("Computer WIN")
    elif user==3 and computer==1:
        print("Computer win")
        pyttsx3.speak("Computer WIN")
    elif user==2 and computer==1:
        print("You win")
        pyttsx3.speak("YOU WIN")
    elif user==1 and computer==3:
        print("You win")
        pyttsx3.speak("YOU WIN")
    elif user==3 and computer==2:
        print("You win")
        pyttsx3.speak("YOU WIN")

