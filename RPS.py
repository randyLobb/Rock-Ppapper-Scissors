import random  
from random import randint 

repeat = True
cursewords = ['fuckyou','fuck you', 'FuckYou', 'fuck','shit','fucker']

while repeat:
    user_choice = input("Rock(1), Paper(2), Scisors(3): Type 1, 2, or 3. type exit to close the game: ")
    Comp_choice = randint(1,3)
    

    if user_choice == "exit":
        break
    if user_choice in cursewords:
        print("well " + user_choice + " too!!!")
    elif user_choice not in['1','2','3']:
        print("I told you to type 1, 2 , or 3!")
    elif int(user_choice) == 1 and Comp_choice == 1:
        print("both chose Rock.it's a tie!")
    elif int(user_choice) == 2 and Comp_choice == 2:
        print("both chose Paper.it's a tie!")
    elif int(user_choice) == 3 and Comp_choice == 3:
        print("both chose scissors. It's a tie!")
    elif int(user_choice) == 1 and Comp_choice == 2:
        print("Computer chose paper, computer wins!")
    elif int(user_choice) == 1 and Comp_choice == 3:
        print("Computer chose scissors. you win!")
    elif int(user_choice) == 2 and Comp_choice == 1:
        print("Computer chose Rock. you win!")
    elif int(user_choice) == 2 and Comp_choice == 3:
        print("Computer chose sciccors. Computer wins!")
    elif int(user_choice) == 3 and Comp_choice == 1:
        print("Computer chose Rock. Computer Wins")
    elif int(user_choice) == 3 and Comp_choice == 2 :
        print("Computer chose paper. you Win!")
    else:
        print("I guess you can't follow simple instructions...")

print("Thanks for playing!")
