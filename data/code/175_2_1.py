import re

def separate_words(sentence):
    return ' '.join(re.split(r'[^\w\s]', sentence))

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test."
    print(separate_words(sample_sentence))