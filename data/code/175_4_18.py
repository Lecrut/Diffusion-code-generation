import re

def extract_words(sentence):
    return re.findall(r'\b\w+\b', sentence)

if __name__ == '__main__':
    sample_sentence = "Python is an interpreted, high-level and general-purpose programming language."
    words = extract_words(sample_sentence)
    print(words)