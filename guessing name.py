print("This Is A Game,Try To Guess My Secret Word ")
print ("The Word Has 4 Letters In It")
print("The Word Is A Name")
secret_word = "amir"
guess = ""
guess_count =  0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("😭😭😭You Lose😭😭😭")
else:
    print("🔥🔥🔥You Win!🔥🔥🔥")
