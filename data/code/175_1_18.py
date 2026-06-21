import re

def tokenize_sentence(sentence):
    return re.findall(r'\b\w+\b', sentence)

if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test sentence, 123."
    result = tokenize_sentence(sample_sentence)
    print(result)