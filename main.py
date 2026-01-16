#Kent Tran
#Group 12
#September 9, 2025
from dictionary import words
import random
import check_input

def display_gallows(num_incorrect):
    """ displays the gallows, state of the gallows depends on the number of incorrect guesses
    args: 
        num_incorrect (int): number of incorrect guesses
    
    returns: None
    
    raises: value rrror if num_incorrect is not between 0 and 6
    """
    gallows_states = [
        """========
||/   |
||
||
||
||""",

        """========
||/   |
||    O
||
||
||""",
        """========
||/   |
||    O
||    |
||
||""",
        """========
||/   |
||    O
||    |
||   /
||""",
        """========
||/   |
||    O
||    |
||   / \\
||""",
        """========
||/   |
||   \\O
||    |
||   / \\
||""",
        """========
||/   |
||   \\O/
||    |
||   / \\
||"""
        
    ]

    print(gallows_states[num_incorrect])

def display_letters(letters):
    """ displays the letters
    args: letters (list): list of letters
    
    returns: none

    raises: 
    """
    print(' '.join(letters))

def get_letters_remaining(incorrect, correct):
    """ displays the letters remaining
    args: incorrect(list): list of the incorrect letters
          correct(list): list of the correct letters
    
    returns: remaining letters that hasn't been guessed yet

    raises:
    """
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']

    used_letters = []
    for letter in incorrect:
        used_letters.append(letter)
        
    for letter in correct:
        if letter != '_':
            used_letters.append(letter)
            
    remaining = []
    for letter in alphabet:
        if letter not in used_letters:
            remaining.append(letter)

    return remaining

def main():
    print("-Hangman-")
    play_again = True
    while play_again:
        word = random.choice(words).upper()

        incorrect_guesses = []
        correct_guesses = ['_'] * len(word)
        num_incorrect = 0
        num_correct = 0

        """starts the game loop"""
        while num_correct < len(word) and num_incorrect < 6:
            print("Incorrect selections:", end=" ")
            if incorrect_guesses:
                display_letters(sorted(incorrect_guesses))
            else:
                print()

            display_gallows(num_incorrect)
            display_letters(correct_guesses)

            print("Letters remaining:", end=" ")
            remaining_letters = get_letters_remaining(incorrect_guesses, correct_guesses)
            display_letters(remaining_letters)

            """gets an input from the user"""
            guess = ""
            valid_guess = False
            while not valid_guess:
                guess = input("Enter a letter: ").upper().strip()

                if len(guess) != 1 or not guess.isalpha():
                    print("That is not a letter.")
                elif guess in incorrect_guesses or guess in correct_guesses:
                    print("You have already used that letter.")
                else:
                    valid_guess = True

            if guess in word:
                print("Correct!")
                
                """fills in all occurrences of the letter"""
                for i in range(len(word)):
                    if word[i] == guess:
                        correct_guesses[i] = guess
                        num_correct += 1
            else:
                print("Incorrect!")
                incorrect_guesses.append(guess)
                num_incorrect += 1

        print("Incorrect selections:", end=" ")
        if incorrect_guesses:
            display_letters(sorted(incorrect_guesses))
        else:
            print()

        display_gallows(num_incorrect)
        display_letters(correct_guesses)

        if num_correct == len(word):
            print("You win!")
        else:
            print("You lose!")
            print(f"The word was: {word}")

        play_again = check_input.get_yes_no("Play again (Y/N)? ")

main()