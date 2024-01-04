def reverse(string):
    return string[::-1]


StringInput = input("Enter a string: ")

while not StringInput.isalpha():
    print("Error Reported! Enter text only.")
    StringInput = input("Enter a string: ")

print(reverse(StringInput))
