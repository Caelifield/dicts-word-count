# put your code here.
#pseudocode
#def 
    #open file
    #create empty dictionary
    #for line in file
        #r strip
        #tokenize by space
        #add each new word to dict / update existing value + 1

    #return dictionary key value pairs

#call function & print

def word_count(filename):
    word_dict = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            words = line.split(" ")
            for word in words:
                word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

wordcount = word_count("test.txt")

for word, number in wordcount.items():
    print(f"{word} {number}")
    