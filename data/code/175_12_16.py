import re

def separate_words(sentence):
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")
    
    words = re.split(r'[ ,.]+', sentence)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_sentence = "Hello, world. This is a test."
    print(separate_words(sample_sentence))