pin = "0456"
guess = "0000"
while pin != guess:
    guess = str(int(guess) + 1)
    if (len(guess) != 4):
        for i in range(4 - len(guess)):
            guess = "0" + guess
print(guess)