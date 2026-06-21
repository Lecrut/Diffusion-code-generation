import re

def validate_input(sentence):
    if not isinstance(sentence, str) or sentence == "":
        raise ValueError("Input must be a non-empty string")

def separate_words(sentence):
    validate_input(sentence)
    words = re.split(r'[ ,.]+', sentence)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_sentence = "Hello, world. This is a test."
    print(separate_words(sample_sentence))