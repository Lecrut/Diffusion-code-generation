import re

def separate_words(sentence):
    return [word for word in re.split(r'[ ,.]+', sentence) if word]

if __name__ == '__main__':
    sample_sentence = "Hello, world. This is a test."
    print(separate_words(sample_sentence))