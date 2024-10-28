#!/usr/bin/env python3
import string
ciphertext2 = "gz xcdaamzhzio kvm yzxvgvbz zno avdwgz!"
L=[]  # empty list
alphabet = string.ascii_lowercase
L.append(alphabet) # L.append('a') # append a to the list
#print(L[0]) # print fist element of L
#L.index('a') # position(s) of element 'a' in the list L
# len(L) # number of element in L
# type(L) # type of variable L
# c = a%b # c = a modulo (b)
# a.lower() # string method --> lowercase
# a.upper() # string method --> uppercase
# M = ''.join(L) # concatenate L element with '' in between


def encrypt(key,plaintext):
    ciphertext=" "
    for i in range(len(plaintext)):
        lettre=plaintext[i]
        if lettre !=" ":
            new_index=(alphabet.index(lettre) + key) % 26
            ciphertext+=alphabet[new_index]
        else:
            ciphertext+=lettre
    return ciphertext
            
                
def decrypt(key, ciphertext):
    plaintext=""
    for i in range(len(ciphertext)):
        lettre=ciphertext[i]
        if lettre in alphabet:
            new_index= (alphabet.index(lettre) - key) % 26
            plaintext+=alphabet[new_index]
        else:
            plaintext+=lettre
    return plaintext 

def attack(ciphertext):
    print("Tentative de décryptage par force brute :")
    for cle in range(len(alphabet)-1):
        plaintext=decrypt(cle,ciphertext)
        print(f"Clé {cle}: {plaintext}")


if __name__ == "__main__":
    message_chiffre=input("Saisir un message à chiffrer : ")
    cle=int(input("Saisir une clé : "))
    while cle<0 or cle>26:
        print("La cle doit etre entre 0 et 26")
        cle=int(input("Saisir une clé : "))

    ciphertext=(encrypt(cle,message_chiffre))
    print("Le message chiffre est : ", ciphertext)

    # message_dechiffrer=input("Saisir le message chiffré : ")
    # cle=int(input("Saisir la clé : "))
    # while cle<0 or cle>26:
    #     print("La cle doit etre entre 0 et 25")
    #     cle=int(input("Saisir une clé : "))

    # plaintext=(decrypt(cle,message_dechiffrer))
    # print("Le message dechiffré est : ", plaintext)

    print("Message chiffré : ",ciphertext2)
    attack(ciphertext2)  # Appel de la fonction d'attaque

