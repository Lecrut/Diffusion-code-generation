import re

def validate_sentence(sentence):
    if not isinstance(sentence, str) or sentence.strip() == "":
        raise ValueError("Invalid input: sentence must be a non-empty string.")

def separate_words(sentence):
    validate_sentence(sentence)
    return re.split(r'[ ,.]+', sentence)

if __name__ == '__main__':
    sample_sentence = "Hello, world. This is a test."
    print(separate_words(sample_sentence))