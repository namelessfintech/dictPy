
import json
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm

# import data from my json file
data = json.load(open("data.json"))

# check variable data type
# print(type(data))

# define a function takes in a key and returns the value
def retrieve(key):
    try:
        if key in data.keys():
             for i in data.get(key):
                print(i)
        elif len(gcm(key, data.keys())) > 0:
            yn = input("Did you mean %s instead? Enter Y is yes or N if no: " %gcm(key,data.keys())[0])
            if yn == "Y" or yn == "y":
                print(data.get(gcm(key, data.keys())[0]))
            elif yn == "n" or yn == "N":
                print("Word does not exist")
            else:
                print("I didn't understand your entry")
        else:
             print("Object does not exist")
    except:
        print("Type error enter a word")

# convert the input to match the storage of data
word = str(input("Please enter a word:")).lower()

retrieve(word)    
print("The program has ended")


