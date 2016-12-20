from tkinter import *
import base64


def encrypt_or_decrypt(event):
    key = keyField.get()

    # Selects between values of radio buttons to determine which mode to use
    if mode.get() == 1:  # Encryption mode
        content = mainField.get()
        enc = []
        for i in range(len(content)):
            key_c = key[i % len(key)]
            encrypt_this = chr(ord(content[i]) + ord(key_c) % 256)
            enc.append(encrypt_this)
        convField.delete(0,"end")
        convField.insert(0, base64.urlsafe_b64encode("".join(enc).encode()).decode())
    elif mode.get() == 2:  # Decryption mode
        content = mainField.get()
        content = base64.urlsafe_b64decode(content).decode()
        dec = []
        for i in range(len(content)):
            key_c = key[i % len(key)]
            decrypt_this = chr((256 + ord(content[i]) - ord(key_c)) % 256)
            dec.append(decrypt_this)
        convField.delete(0,"end")
        convField.insert(0, ("".join(dec)))


# Main Tk Object initialization
root = Tk()
root.geometry("200x190")
root.title("EncryptorTK")
frame = Frame(root)

# Creating the message field for the text
mainField = Entry(root)
mainField.insert(0, "Enter Text.")
mainField.pack(side=TOP,anchor=W)

# Creating the message field for the key
keyField = Entry(root)
keyField.insert(0, "Enter Key.")
keyField.pack(side=TOP, anchor=W)

# Creating the radio button options for selecting either encryption or decryption
mode = IntVar()
but1 = Radiobutton(root, text="Encrypt.", variable=mode, value=1).pack(anchor=W)
but2 = Radiobutton(root, text="Decrypt.", variable=mode, value=2).pack(anchor=W)

# Creating the field for the converted text
convField = Entry(root)
convField.pack(side=BOTTOM, anchor=W)

# Action button that runs the program
enterButton = Button(root, text="Run Program")
enterButton.bind("<Button-1>", encrypt_or_decrypt)
enterButton.pack(side=BOTTOM, anchor=W)

# Runs the actual TK program
root.mainloop()
