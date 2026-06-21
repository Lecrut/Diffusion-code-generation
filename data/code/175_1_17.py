import re

def tokenize_string(sentence):
    return re.findall(r'\b\w+\b', sentence)

if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test sentence, 123."
    result = tokenize_string(sample_sentence)
    print(result)