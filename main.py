import random

def hangman():
    words = ["python", "programming", "hangman", "challenge", "openai"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Willkommen zum Hangman-Spiel!")
    print(" ".join(guessed_word))
    print(f"Du hast {attempts} Versuche.\n")

    while attempts > 0 and "_" in guessed_word:
        guess = input("Gib einen Buchstaben ein: ").lower()

        if guess in guessed_letters:
            print("Du hast diesen Buchstaben bereits geraten. Versuche es mit einem anderen.")
        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            guessed_letters.append(guess)
            print("Gut gemacht! Der Buchstabe ist im Wort.")
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f"Falsch! Du hast noch {attempts} Versuche.")

        print(" ".join(guessed_word))
        print(f"Bisher geratene Buchstaben: {', '.join(guessed_letters)}\n")

    if "_" not in guessed_word:
        print("Glückwunsch! Du hast das Wort erraten.")
    else:
        print(f"Du hast verloren. Das Wort war '{word}'.")

if __name__ == "__main__":
    hangman()
