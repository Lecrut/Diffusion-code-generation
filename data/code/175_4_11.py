import re

def extract_words(sentence):
    return re.findall(r'\b\w+\b', sentence)

if __name__ == '__main__':
    sample_sentence = "This is a sample sentence for testing"
    words = extract_words(sample_sentence)
    print(words)