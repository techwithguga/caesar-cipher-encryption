alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#function to take text and shift and return the encrypted text
# def encrypt(plain_text, shift_amount):

#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         #last letters position start from 0
#         if new_position > 25:
#             new_position = new_position - 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is : {cipher_text}")

# def decrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         #last letters position start from 0
#         if new_position < 0:
#             new_position = new_position + 26
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The decoded text is : {cipher_text}")

# if direction=="encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction=="decode":
#     decrypt(plain_text=text, shift_amount=shift)

def caesar(start_text, shift_amount, cipher_direction):
    
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        
        if cipher_direction =="encode":
            new_position = position + shift_amount
            if new_position > 25:
                new_position = new_position - 26
        elif cipher_direction =="decode":
            new_position = position - shift_amount
            if new_position < 0:
                new_position = new_position + 26
        new_letter = alphabet[new_position]
        end_text += new_letter
    print(f"The encoded text is : {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)