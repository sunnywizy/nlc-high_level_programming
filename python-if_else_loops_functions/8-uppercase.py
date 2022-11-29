#!/usr/bin/python3
def uppercase(str1):
    for i in range(len(str1)):
        char = ord(str1[i])
        if char >= 97 and char <= 122:
            char = char - 32
        print("{}".format(chr(char)), end="")
    print()