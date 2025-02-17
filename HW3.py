
from string import punctuation

#The Dangerous inheretance

import requests
book = requests.get("https://www.gutenberg.org/cache/epub/75383/pg75383-images.html")
lines = book.text.split("\n")
punctuation_remove = ",.!?:;"
punctuation_space = "'\"()[]=-_"
unique_words_danger = {}
for line in lines:
    for c in punctuation_remove:
        line = line.replace(c, "")
    for c in punctuation_space:
        line = line.replace(c," ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words_danger[word] = unique_words_danger.get(word,0)+1

print(f"The number of unique words in 'The Dangerous Inheritance' is {len(unique_words_danger)}")

#Needwood Forest

book = requests.get("https://www.gutenberg.org/cache/epub/75378/pg75378-images.html")
lines = book.text.split("\n")
punctuation_remove = ",.!?:;"
punctuation_space = "'\"()[]=-_"
unique_words_needwood = {}
for line in lines:
    for c in punctuation_remove:
        line = line.replace(c, "")
    for c in punctuation_space:
        line = line.replace(c," ")
    words = line.split()
    for word in words:
        word = word.lower()
        unique_words_needwood[word] = unique_words_needwood.get(word,0)+1

print(f"The number of unique words in 'Needwood Forest' is {len(unique_words_needwood)}")


if len(unique_words_danger) > len(unique_words_needwood):
    print(f"The book 'The Dangerous Inheritance' contains more unique words with a total of {len(unique_words_danger)} unique words")
elif len(unique_words_needwood) > len(unique_words_danger):
    print(f"The book 'Needwood Forest' contains more unique words with a total of {len(unique_words_danger)} unique words")
else:
    print("Both books have the same amount of unique words")

    #test