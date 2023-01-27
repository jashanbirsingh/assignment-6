def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.lower().replace(" ","")
    return set(sentence).issuperset(alphabet)

sentence = input("Enter a sentence: ")
if(is_pangram(sentence) == True):
    print(sentence," is a pangram.")
else:
    print(sentence," is not a pangram.")