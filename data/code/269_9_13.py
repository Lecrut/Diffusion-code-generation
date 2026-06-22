import re

def extract_punctuation(text):
    punctuation = []
    for char in text:
        if not char.isalnum() and not char.isspace():
            punctuation.append(char)
    return punctuation

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? This is a test."
    result = extract_punctuation(sample_string)
    print(result)