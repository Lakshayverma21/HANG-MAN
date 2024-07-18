import random

with open("/Users/lakshayverma.LV/Desktop/CODING/GIT PROJECTS/GIT HANG-MAN/WORDS.txt", "r") as file:
    words = file.read().splitlines()

word = random.choice(words)
total_chances = 7
guessed_word = "-" * len(word)

print("Welcome to Hangman!")
print(f"Your word: {guessed_word}")

while total_chances != 0:
    print("\nCurrent word:", guessed_word)
    letter = input("Guess a letter: ").upper()

    if len(letter) != 1 or not letter.isalpha():
        print("Please guess a single letter.")
        continue

    if letter in word:
        new_guessed_word = ""
        for index in range(len(word)):
            if word[index] == letter:
                new_guessed_word += letter
            else:
                new_guessed_word += guessed_word[index]
        guessed_word = new_guessed_word

        if guessed_word == word:
            print("Congratulations, you won!!!")
            break

    else:
        total_chances -= 1
        print("Incorrect guess.")
        print(f"The remaining chances are: {total_chances}")

else:
    print("GAME OVER")
    print("You Lose")
    print("All the chances are exhausted.")

print("The word was:", word)