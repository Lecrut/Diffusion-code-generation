import re

def is_punctuation(char):
    return char in string.punctuation

def isolate_punctuation(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    isolated_text = ''.join(' ' if is_punctuation(char) else char for char in text)
    return isolated_text

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))