import re

def extract_words(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    return words

if __name__ == '__main__':
    sample_sentence = "Hello, World! This is a test."
    print(extract_words(sample_sentence))