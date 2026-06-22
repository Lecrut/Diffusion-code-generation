import re

def extract_punctuation(text):
    punctuation = []
    for char in text:
        if not char.isalnum() and char != ' ':
            punctuation.append(char)
    return list(dict.fromkeys(punctuation))

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? This is a test."
    result = extract_punctuation(sample_string)
    print(result)