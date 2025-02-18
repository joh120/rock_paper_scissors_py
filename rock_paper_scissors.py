import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose: rock, paper, or scissors.")
    user_choice = input()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("The computer chose: " + computer_choice)
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    else:
        return "You lose!"

print(rock_paper_scissors())
