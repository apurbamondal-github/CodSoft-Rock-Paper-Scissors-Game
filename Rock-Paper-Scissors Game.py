import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to update the game state
def play(user_choice):
    global user_score, computer_score

    # Generate computer's choice
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    # Determine the result
    result = determine_winner(user_choice, computer_choice)

    # Update scores
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1

    # Update the GUI with choices and results
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Let's Play Again!")
    score_label.config(text=f"Score: You {user_score} - Computer {computer_score}")

# Initialize the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Initialize scores
user_score = 0
computer_score = 0

# Create labels and buttons
title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 20))
title_label.pack(pady=10)

result_label = tk.Label(window, text="Choose your move!", font=("Arial", 16))
result_label.pack(pady=10)

score_label = tk.Label(window, text=f"Score: You {user_score} - Computer {computer_score}", font=("Arial", 14))
score_label.pack(pady=10)

# Create buttons for rock, paper, scissors
rock_button = tk.Button(window, text="Rock", width=15, height=2, font=("Arial", 14), command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=15, height=2, font=("Arial", 14), command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=15, height=2, font=("Arial", 14), command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Add a reset button to restart the game
reset_button = tk.Button(window, text="Reset Game", width=15, height=2, font=("Arial", 14), command=reset_game)
reset_button.pack(pady=20)

# Run the application
window.mainloop()
