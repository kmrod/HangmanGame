import tkinter as tk
from tkinter import messagebox
import random

# List of words to guess for Hangman
words = ["abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "bagpipes",
         "bandwagon", "banjo", "bayou", "beekeeper", "blizzard", "boggle", "bookworm", "buckaroo",
         "buffalo", "cobweb", "croquet", "crypt", "daiquiri", "duplex", "embezzle", "espionage",
         "exodus", "faking", "fishhook", "fixable", "flapjack", "fuchsia", "funny", "galaxy",
         "gazebo", "gizmo", "haiku", "haphazard", "hyphen", "icebox", "injury", "ivory", "ivy",
         "jackpot", "jaundice", "jaywalk", "jelly", "jigsaw", "jiujitsu", "jinx", "jockey",
         "jogging", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki",
         "kilobyte", "kiosk", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury", "lymph",
         "matrix", "microwave", "mystify", "nightclub", "onyx", "oxidize", "oxygen", "pajama",
         "peekaboo", "phlegm", "pixel", "polka", "psyche", "puppy", "puzzling", "quartz", "queue",
         "quiz", "quizzes", "quorum", "rhythm", "scratch", "snazzy", "sphinx", "spritz", "staff",
         "strength", "stretch", "subway", "swivel", "syndrome", "topaz", "transcript", "transplant",
         "twelfth", "unknown", "unworthy", "unzip", "vaporize", "vixen", "vodka", "vortex", "walkway",
         "waltz", "wave", "wavy", "wheezy", "whiskey", "wizard", "wristwatch", "xylophone", "youthful",
         "yummy", "zigzag", "zipper", "zodiac", "zombie"]

# Create hints:
hints = {}
for word in words:
    if "z" in word:
        hint = "Contains the letter Z"
    elif word in {"banjo", "jukebox", "kazoo", "xylophone", "waltz", "jazz"}:
        hint = "Related to music"
    elif word in {"wizard", "zombie", "crypt", "sphinx", "mystify"}:
        hint = "Magical or mysterious"
    elif word in {"bookworm", "quiz", "quizzes", "transcript", "matrix", "lengths"}:
        hint = "Related to school or learning"
    elif word in {"daiquiri", "vodka", "flapjack", "icebox", "microwave", "pajama"}:
        hint = "Something you'd find at home"
    elif word in {"puppy", "peekaboo", "yummy", "joyful"}:
        hint = "Cute or playful"
    elif word in {"oxygen", "larynx", "lymph", "phlegm", "injury"}:
        hint = "Related to the human body"
    elif word in {"onyx", "topaz", "quartz"}:
        hint = "Gem"
    elif word in {"awkward", "absurd", "haphazard", "askew"}:
        hint = "Describes something odd or messy"
    else:
        hint = f"A word starting with '{word[0].upper()}'"
    hints[word] = hint

# Initialize variables:
selected_word = random.choice(words)
letters_used = []
lives = 6

# Create window:
window = tk.Tk()
window.title("Let's Play Hangman!")

# GUI Elements
title = tk.Label(window, text="HANGMAN GAME", font=("Helvetica", 28, "bold"), fg="pink")
word_label = tk.Label(window, text="", font=("Helvetica", 24))
lives_label = tk.Label(window, text="", font=("Helvetica", 16))
hint_label = tk.Label(window, text="", font=("Helvetica", 14, "italic"), fg="green")
used_label = tk.Label(window, text="Used Letters: ", font=("Helvetica", 14))
get_letter = tk.Entry(window, font=("Helvetica", 16))
canvas = tk.Canvas(window, width=500, height=300)
enter_button = tk.Button(window, text="Enter", command= lambda: lets_play())
new_game_label = tk.Label(window, text="Start a new game:", font=("Helvetice", 12))
reset_button = tk.Button(window, text="Reset", command=lambda: reset())

# Define win() function to check if the player has won:
def win():
    return all(letter in letters_used for letter in selected_word)

# Define loss() function to check if the player has lost:
def loss():
    return lives == 0

# Define disable_input() and enable_input() function to prevent extra guesses after the game is over
def disable_input():
    get_letter.config(state="disabled")
    enter_button.config(state="disabled")

def enable_input():
    get_letter.config(state="normal")
    enter_button.config(state="normal")

# Define show_progress() function to update the word display with correctly guessed letters
def show_progress():
    show_word = ""
    for letter in selected_word:
        show_word += letter if letter in letters_used else "-"
    word_label.config(text=show_word)

# Define show_used_letters() function to display letters that player has already guessed
def show_used_letters():
    used_label.config(text="Used letters: " + " ".join(letters_used))

# Define show_lives() function to display how many lives are remaining
def show_lives():
    color = "green" if lives > 3 else "orange" if lives > 1 else "red"
    lives_label.config(text=f"Lives remaining: {lives}", fg=color)

# Define hangman_figure() function which draws hangman based on how many lives left
def hangman_figure():
    canvas.delete("hangman")
    if lives < 6:
        canvas.create_oval(225, 120, 275, 170, width=3, tags="hangman")
    if lives < 5:
        canvas.create_line(250, 170, 250, 250, width=3, tags="hangman")
    if lives < 4:
        canvas.create_line(250, 190, 220, 210, width=3, tags="hangman")
    if lives < 3:
        canvas.create_line(250, 190, 280, 210, width=3, tags="hangman")
    if lives < 2:
        canvas.create_line(250, 250, 220, 300, width=3, tags="hangman")
    if lives < 1:
        canvas.create_line(250, 250, 280, 300, width=3, tags="hangman")

# Define lets_play() function to allow player to guess the word:
def lets_play():
    global lives
    letter = get_letter.get().lower()
    get_letter.delete(0, tk.END)
    if not letter.isalpha() or len(letter) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single letter")
        return
    if letter in letters_used:
        messagebox.showinfo("Try again!", f"You already guessed '{letter}'")
        return
    letters_used.append(letter)
    if letter in selected_word:
       show_progress()
       show_used_letters()
       if win():
           word_label.config(text=selected_word)
           messagebox.showinfo("Congratulations!", f"You Won!! Hurray!! The word was {selected_word}")
           disable_input()
    else:
        lives -= 1
        hangman_figure()
        show_lives()
        show_used_letters()
        if loss():
            word_label.config(text=selected_word)
            messagebox.showinfo("Game Over", f"Sorry :( You lost, try again! The word was {selected_word}")
            disable_input()
    get_letter.focus_set()

# Define reset() function which resets the game all the way to the beginning and starts a new round
def reset():
    global selected_word, letters_used, lives
    enable_input()
    selected_word = random.choice(words)
    letters_used = []
    lives = 6
    show_progress()
    show_lives()
    show_used_letters()
    hangman_figure()
    hint_label.config(text="Hint: " + hints[selected_word])
    get_letter.focus_set()

# Update canvas size for more space
canvas.config(width=500, height=400)

# Draw Gallows
canvas.create_line(150, 350, 350, 350, width=3, tags="gallows")
canvas.create_line(300, 350, 300, 50, width=3, tags="gallows")
canvas.create_line(300, 50, 250, 50, width=3, tags="gallows")
canvas.create_line(250, 50, 250, 120, width=3, tags="gallows")

# Pack GUI Elements
title.pack(pady=10)
word_label.pack(pady=10)
lives_label.pack()
hint_label.pack(pady=5)
used_label.pack(pady=5)
canvas.pack()
guess_label = tk.Label(window, text="Guess a letter: ", font=("Helvetica", 16))
guess_label.pack()
get_letter.pack(pady=10)
enter_button.pack()
new_game_label.pack(pady=(20, 0))
reset_button.pack(pady=(0, 10))

# Update Displays
show_progress()
show_lives()
hangman_figure()

# Run
window.mainloop()














