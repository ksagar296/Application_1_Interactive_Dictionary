import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

#####################################################################################
# SequenceMatcher(None,"rainn","rain").ratio()
# >>> help(get_close_matches)
# Help on function get_close_matches in module difflib:
#
# get_close_matches(word, possibilities, n=3, cutoff=0.6)
#   Use SequenceMatcher to return list of the best "good enough" matches.
#   word is a sequence for which close matches are desired (typically astring).
#####################################################################################

data = json.load(open("D:\Python_Learning\Application_1_Interactive_Dictionary\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s Instead? Enter Y if yes or N if no: " % get_close_matches(w,data.keys())[0])   ## To get only one i.e. first close match
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "Word does Not Exist, Please Double check your word"
        else:
            return "We didn't understand your Entry ...."
    else:
        return "Word does Not Exist, Please Double check your word"

word = input("Enter your Word : ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)