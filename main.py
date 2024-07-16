import random
import time

op1 = ["rock","paper","scissor"]
print("Welcome to Rock, Paper, Scissor game")
while True:
  
  com_choice = random  .choice(op1)
  user_input = input("\nEnter Your Choice From Rock Paper And Scissor: ").lower()
  if user_input == 'q' or user_input == '0':
    print("\nThanks for playing")
    break
  elif user_input not in op1:
    print("\nEnter the value from the given options")
    break
    
  else:
    print("\nComputer is choosing...")
    time.sleep(2)
    print(f"\nComputer choice is {com_choice}")

  if user_input == com_choice:
    print("\nIt's a tie")

  elif user_input == "rock" and com_choice == "scissor" or \
  user_input == "paper" and com_choice == "scissor" or \
  user_input == "scissor" and com_choice == "rock":
    print("\nYou Lose")
    
    
  else:
    print("\nYou win the game")
