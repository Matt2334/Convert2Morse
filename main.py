morsecode= ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__','_.', '___', '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..']
alphabet= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def encoder(message):
     end_result = ""
     sentence = message.split(' ')
     for x in range(len(sentence)):
# loops through all of the words in the sentence
        for letter in sentence[x]:
           # loops through all of the letters in each word
            position = alphabet.index(letter.capitalize())
            encoded_letter = morsecode[position]
            end_result += encoded_letter
            # Adds a space in between each letter for clarity
            end_result += end_result.join(" ")
        # Separates each word by a *
        end_result += end_result.join('*')
     print(f"Your new message is {end_result}")
def decoder(morse):
    starter_word = ""
    split_morse = morse.split('*')
    for x in range(len(split_morse)):
        separated = split_morse[x].split(' ')
        separated = list(filter(None, separated))
        for char in separated:
            position = morsecode.index(char)
            decoded_letter = alphabet[position]
            starter_word+= decoded_letter
        starter_word+= starter_word.join(" ")

    print(f"Your decoded message is: {starter_word.capitalize()}")

ask = input("Do you want to encode or decode a message? Type encode or decode to select: ")
if ask=="encode":
    message = input("Hello and Welcome to the Morse Code Generator\nType the word to begin: ")
    encoder(message)
else:
    morse = input("Type the encoded message to begin: ")
    decoder(morse)
