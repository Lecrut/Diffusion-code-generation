import re

def split_sentence(sentence):
    words = re.split(r'[ ,.]+', sentence)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_sentence = "Split, this .sentence correctly please?"
    words = split_sentence(sample_sentence)
    print(words)