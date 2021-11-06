# 7. Напишите программу, которая создает файл с N случайными буквами a-zA-Z.
import random

# get string size
N = random.randint(0, 10)
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# create a string
resultString = ''

i = 1
while i <= N:
    n = random.randint(0, len(ascii_letters))
    resultString = resultString + ascii_letters[n]
    i += 1

# write to a new file
fwrite = open("d:\pyton\lab6\lab_result.txt", "w")
fwrite.write(resultString)
