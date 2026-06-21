import re

ALPHABETIC_PATTERN = re.compile(r'[a-zA-Z\s]+')

def tokenize_sentence(sentence):
    return ALPHABETIC_PATTERN.findall(sentence)

if __name__ == '__main__':
    sample_sentence = "Hello World! This is a test sentence with numbers 123."
    result = tokenize_sentence(sample_sentence)
    print(result)