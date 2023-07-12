sentence = "hello world! this is a test sentence."

# Convert the sentence into a list of characters
characters = list(sentence)

# Iterate through the characters and capitalize the letter after each space
for i in range(len(characters) - 1):
    if characters[i] == ' ':
        characters[i + 1] = characters[i + 1].upper()

# Construct the capitalized sentence
capitalized_sentence = ""
for char in characters:
    capitalized_sentence += char

print(capitalized_sentence)
