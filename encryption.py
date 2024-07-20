import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)


while True:
    choice=input("Enter 0 for encryption and 1 for deccryption: ")
    if choice=="0":
            
        #encryption...!
        plain_text=input("Enter the message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text+=key[index]

        print(f"original message: {plain_text}")
        print(f"encrypted message: {cipher_text}")
    elif choice=="1":
        cipher_text=input("Enter the message to decrypt: ")
        plain_text = ""

        for letter in cipher_text:
            index = key.index(letter)
            plain_text+=chars[index]

        print(f"encrypted message: {cipher_text}")
        print(f"original message: {plain_text}")

    print("\nHere we go again...!\nyou can do CTRL + x for exit this loop...!\n")