import string

mylist =[]
lowercase = list(string.ascii_lowercase)
string = input("Enter a string. ")
string = string.lower()

for char in string:
    if char.isalpha() == True:
        mylist.append(char)
        
mylist = list(set(mylist))
mylist.sort()
if(mylist == lowercase):
    print("The entered string is a pangram.", end="")
else:
    print("The entered string is not a pangram.", end="")
