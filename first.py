def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
       
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

n = input(" ENTER THE TASK YOU WANT TO ENCRYPT  : ")

s = 5
print ("CURRENT DATA " + n)
print ("SHIFTED DATA : " + str(s))
print ("ENCRYPTED DATA : " + encrypt(n,s))

def decrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]
 
        if (char.isupper()):
            result += chr((ord(char) - s + 65) % 26 + 65)
 
       
        else:
            result += chr((ord(char) - s + 97) % 26 + 97)
 
    return result

n = input(" ENTER THE TASK YOU WANT TO DECRYPT : ")

s = 5
print ("CURRENT" + n)
print ("SHIFTED DATA : " + str(s))
print ("DECRYPTED DATA: " + decrypt(n,s))
print("this is the changed py file : ")
