import tkinter as tk
import random

# ----------------- Game Logic -----------------
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)

    result_text = f"You chose {user_choice}, Computer chose {comp_choice}.\n"

    if user_choice == comp_choice:
        result_text += "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result_text += "You Win!"
        user_score += 1
    else:
        result_text += "Computer Wins!"
        computer_score += 1

    result_label.config(text=result_text)
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

# ----------------- GUI Setup -----------------
root = tk.Tk()
root.title("🪨 Rock - 📄 Paper - ✂️ Scissors")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

# Title
tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 16, "bold"), bg="#f2f2f2").pack(pady=10)

# Instructions
tk.Label(root, text="Choose your move:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack()

tk.Button(button_frame, text="🪨 Rock", width=10, font=("Arial", 12), command=lambda: play("Rock")).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="📄 Paper", width=10, font=("Arial", 12), command=lambda: play("Paper")).grid(row=0, column=1, padx=10, pady=10)
tk.Button(button_frame, text="✂️ Scissors", width=10, font=("Arial", 12), command=lambda: play("Scissors")).grid(row=0, column=2, padx=10, pady=10)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2", fg="blue")
result_label.pack(pady=10)

# Scoreboard
score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12), bg="#f2f2f2", fg="green")
score_label.pack(pady=10)

# Quit Button
tk.Button(root, text="Exit Game", font=("Arial", 12), bg="red", fg="white", command=root.quit).pack(pady=20)

root.mainloop()
