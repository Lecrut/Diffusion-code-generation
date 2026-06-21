import re

def tokenize_sentence(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', sentence)
    return words

if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test sentence with numbers 123."
    result = tokenize_sentence(sample_sentence)
    print(result)