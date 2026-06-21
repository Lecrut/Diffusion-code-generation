import re

def separate_words(sentence):
    return re.split(r'\s+|[,.]', sentence)

if __name__ == '__main__':
    sample_sentence = "Hello, world. This is a test."
    print(separate_words(sample_sentence))