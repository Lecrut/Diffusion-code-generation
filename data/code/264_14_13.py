import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def extract_words(text):
    return re.findall(r'\b\w+\b', text)

def remove_duplicates(words):
    return set(words)

def tokenize_and_filter(text):
    validate_input(text)
    words = extract_words(text)
    unique_words = remove_duplicates(words)
    return list(unique_words)

if __name__ == '__main__':
    sample_text = "Hello World! This is a test string, with numbers 123 and symbols @#$."
    result = tokenize_and_filter(sample_text)
    print(result)