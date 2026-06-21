import re

def validate_sentence(sentence):
    if not isinstance(sentence, str) or not sentence.strip():
        raise ValueError("Input must be a non-empty string")

def separate_words(sentence):
    validate_sentence(sentence)
    return [word for word in re.split(r'[ ,.]+', sentence) if word]

if __name__ == '__main__':
    sample_sentence = "Hello, world. This is a test."
    print(separate_words(sample_sentence))