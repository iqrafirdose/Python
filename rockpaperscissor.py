#rock,paper and scissors
print("Hey! Let's play a game with me")
print(" ")
print("----***Rock,Paper and scissors***----")
print(" \n ")
print("In this game ,two players do their hand structures shows rock,paper and scissors")
print("player and computer")
print(".         ")
print ("*****Game rules*******")
print("Rock Vs paper:      paper win!!! \n ___paper wraps rock___")
print("Paper Vs scissors:  scissors win!!!! \n ___scissors cuts paper___")
print("Scissors Vs Rock:   Rock win !!!\n ____Rock smashes scissors___")
print("  \n  ")
print("   Let's start the game.  ")
gamer=input("Enter your name :")
print (f"{gamer} you are playing with computer")
computer=0
player=0
i=1
chance=int(input ("How many times do you want to play  "))
while i<=chance:
   human=input("Enter your choice:")
   print (f"{gamer}:{human}")
   import random
   computer_choice=random.choice(["rock","paper","scissors"])
   
 
   if human=="rock":
     print(f"Computer :{computer_choice}")
     if computer_choice=="paper":
        print("Computer wins")
        computer+=1
     elif computer_choice=="scissors":
        print (f"{gamer} wins")
        player+=1
     else:
        print("It's a tie")


   
   elif human=="paper":
     print(f"Computer :{computer_choice}")
     if computer_choice=="scissors":
        print("Computer wins")
        computer+=1
     elif computer_choice=="rock":
        print(f"{gamer} wins")
        player+=1
     else:
        print("It's a tie")
   
   elif human == "scissors":
     print(f"Computer:{computer_choice}")
     if computer_choice == "rock":
        print("Computer wins")
        computer+=1
     elif computer_choice=="paper": 
        print (f"{gamer} wins")
        player+=1
     else:
        print("It's a tie")

   else: 
    print(" please enter correctly")
   i+=1
print("*****score board******")
print(f"{gamer}:{player} Computer:{computer}")
if player>computer:
  print(f" {gamer} wins the game🏆🏆")
if player<computer:
  print("buzzy wins the game🏆🏆")
if player==computer:
  print ("oops! It's a tie  play again ")
