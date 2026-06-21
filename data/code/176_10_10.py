import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def extract_words(text):
    validate_input(text)
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_text = "This is a test string with words, including multiple sentences!"
    print(extract_words(sample_text))