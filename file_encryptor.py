def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Enter Choice: ")

filename = input("Enter File Name: ")

shift = 3

try:

    with open(filename, "r") as file:
        content = file.read()

    if choice == "1":

        encrypted_text = encrypt(content, shift)

        with open("encrypted.txt", "w") as file:
            file.write(encrypted_text)

        print("File Encrypted Successfully!")
        print("Saved as encrypted.txt")

    elif choice == "2":

        decrypted_text = decrypt(content, shift)

        with open("decrypted.txt", "w") as file:
            file.write(decrypted_text)

        print("File Decrypted Successfully!")
        print("Saved as decrypted.txt")

    else:
        print("Invalid Choice!")

except FileNotFoundError:
    print("File Not Found!")