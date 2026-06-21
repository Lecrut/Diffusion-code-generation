import re

def split_sentence(sentence):
    return re.split(r'[ ,.]+', sentence)

if __name__ == '__main__':
    test_sentence = "Split, this .sentence correctly please?"
    words = split_sentence(test_sentence)
    print(words)