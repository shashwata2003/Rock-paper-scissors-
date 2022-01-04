import random

score_user=0
comp_user=0
draws=0

options = ["rock", "paper", "scissors"]
while True:
    a=input("Type rock/paper/scissors or Q to quit: ") #this is the users pick
    if a=='q':
        print('Thank you for playing')
        break
    if a not in options:
        print('Invalid Input')
        continue
    b=random.randint(0,2)
    c=options[b] #Thii is the comps pick
    print("Computer picked", c + ".")

    if a == "rock" and c == "scissors":
        print("You won!")
        score_user += 1

    elif a == "paper" and c == "rock":
        print("You won!")
        score_user += 1

    elif a == "scissors" and c == "paper":
        print("You won!")
        score_user += 1
    elif a=='rock' and c=='rock':
        print('Draw!')
        draws=draws+1
    elif a=='paper' and c=='paper':
        print('Draw!')
        draws=draws+1
    elif a=='scissors' and c=='scissors':
        print('Draw!')
        draws=draws+1
    else:
        print("You lost!")
        comp_user += 1
print("You won", score_user, "times.")
print("The computer won", comp_user, "times.")
print("The number of Draws are ", draws)
print("Thank you for playing!")