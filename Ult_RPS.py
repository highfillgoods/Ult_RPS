import random
# Ultimate paper, rock, scissors game to keep track of score against computer.
# If you and the computer pick the same option the next round will increase points to x2. 
# Once someone wins the score will go back to 1x points.
# Push q to quit and show score.


# Starting points for user
user_wins = 0
# Starting points for computer
computer_wins = 0
# Standard adding points amount for win
current_add_points = 1
# Current options to choose from
options=["rock","paper","scissors","fire","snake","human","tree","wolf","sponge","air","water","dragon","devil","lightning","gun"]


while True:
    # start the game enter input from options or q to quit and exit main loop.
    user_input = input("Pick from: rock, paper, scissors, fire, snake, human, tree, wolf, sponge, air, water, dragon, devil, lightning, gun... (Type 'Q' to Quit): ").lower()
    if user_input == "q":
        break
    
    # if user picks words not from the list.
    if user_input not in options:
        print("type a valid option next time")
        
    # computer pick random number and pair it with the list of options(0, 14)
    # set random.randint(0, 0) to only have computer choose rock
    random_number = random.randint(0, 14)

    # rock: 0,paper: 1,scissors: 2,fire: 3,snake: 4,human: 5,tree: 6,wolf: 7,sponge: 8,air: 9,water: 10,dragon: 11,devil: 12,lightning: 13,gun: 14]
    computer_pick = options[random_number]
    print("computer chose", computer_pick)

    # when user and computer pick same option. the next round is 2x points
    if user_input == "rock" and computer_pick == "rock":
        print("..Tie, next round x2 points")
        current_add_points = current_add_points * 2 

    # If user select rock and computer pick sponge, wolf, ext. User wins and gets current point/s added to the score
    elif user_input == "rock" and computer_pick in ["sponge", "wolf", "tree", "human", "snake", "scissors", "fire", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1  # reset current point count to 1
        
    elif user_input == "paper" and computer_pick == "paper":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2   

    elif user_input == "paper" and computer_pick in ["rock", "gun", "lighting", "devil", "dragon", "water", "air", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1  

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "scissors" and computer_pick in ["snake", "human", "tree", "wolf", "sponge", "paper", "air", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1  

    # rock paper scissors ULTIMATE portion below are extra options.
    elif user_input == "fire" and computer_pick == "fire":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "fire" and computer_pick in ["paper", "sponge", "wolf", "tree", "human", "snake", "scissors", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1        

    elif user_input == "snake" and computer_pick == "snake":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "snake" and computer_pick in ["human", "tree", "wolf", "sponge", "paper", "air", "water", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1             

    elif user_input == "human" and computer_pick == "human":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "human" and computer_pick in ["tree", "wolf", "sponge", "paper", "air", "water", "dragon", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1   

    elif user_input == "tree" and computer_pick == "tree":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "tree" and computer_pick in ["wolf", "sponge", "paper", "air", "water", "dragon", "devil", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1        
        
    elif user_input == "wolf" and computer_pick == "wolf":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "wolf" and computer_pick in ["sponge", "paper", "air", "water", "dragon", "devil", "lightining", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1   

    elif user_input == "sponge" and computer_pick == "sponge":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "sponge" and computer_pick in ["paper", "air", "water", "dragon", "devil", "lightining", "gun", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1    

    elif user_input == "air" and computer_pick == "air":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "air" and computer_pick in ["water", "dragon", "devil", "lightining", "gun", "rock", "fire", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1   

    elif user_input == "water" and computer_pick == "water":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "water" and computer_pick in ["dragon", "devil", "lightining", "gun", "rock", "fire", "scissors", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1   

    elif user_input == "dragon" and computer_pick == "dragon":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "dragon" and computer_pick in ["devil", "lightining", "gun", "rock", "fire", "scissors", "snake", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1 

    elif user_input == "devil" and computer_pick == "devil":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "devil" and computer_pick in ["lightining", "gun", "rock", "fire", "scissors", "snake", "human", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1 

    elif user_input == "lighting" and computer_pick == "lighting":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "lighting" and computer_pick in ["gun", "rock", "fire", "scissors", "snake", "human", "tree", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1 

    elif user_input == "gun" and computer_pick == "gun":
        print("Tie, next round x2 points")
        current_add_points = current_add_points * 2  
        
    elif user_input == "gun" and computer_pick in ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", False]:
        print("You win!")
        user_wins += current_add_points
        current_add_points = 1 


    # if all options above are not met then user lost, and computer won and is awarded current point/s.
    else:
        print("You lost!")
        computer_wins = computer_wins + current_add_points 
        current_add_points = 1  # reset current point count to 1


print("...Your points", user_wins,)
print("...The computer's points", computer_wins)
print(".....See you later......")


