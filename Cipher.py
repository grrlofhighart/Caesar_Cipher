# Create empty lists to hold dictionary and key
alpha = []
key = []

# Set up rules for the dictionary
alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]

# Create empty list for path
path = []
i = 0
while i < 1:
    try:
        # Ask user if they are encrypting or decrypting
        question = (int(input("Enter 1 to Encrypt OR Enter 2 to Decrypt: ")))
        if question >= 1 and question <= 2:
            path.append(question)
            i = i + 1
        else:
            print("Invalid input. ")
    except ValueError:
        print("Invalid input. ")
while i < 2:
    try:
        # Ask user to provide shift value
        shift = (int(input("What is the shift? ")))
        i = i + 1
    except ValueError:
        print("Invalid input. Please enter a valid number")

# Checking work
# print(path)

# Set up rules for the key
for x in alpha[shift:] + alpha[:shift]:
    key.append(x)

# print(alpha)
# print(key)

# Combine the two lists to create the dictionary
if path == [1]:
    cipher = dict(zip(alpha, key))
else:
    cipher = dict(zip(key, alpha))

# print(cipher)

# Ask user for a sentence
sentence = input("Please enter a sentence: ")

# Convert the sentence to all lower case for simplicity
sentence = sentence.lower()

# Create empty list to store the converted text
output = []

# Convert input to encrypted/decrypted text
for character in sentence:
    if character in cipher:
        output.append(cipher[character])
    else:
        output.append(character)

# Join items in output list to create string of encrypted/decrypted text
sentence = "".join(output)

# Print encrypted/decrypted message
print(sentence)