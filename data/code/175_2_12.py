import re

def separate_words(sentence):
    return re.sub(r'[^\w\s]', ' ', sentence).split()

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test. Multiple...delimiters?"
    print(separate_words(sample_sentence))