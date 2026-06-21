import re

def validate_input(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

def extract_words(text):
    return re.findall(r'\b\w+\b', text.lower())

def filter_unique(words):
    seen = set()
    unique_words = []
    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)
    return unique_words

def tokenize_text(text):
    validate_input(text)
    words = extract_words(text)
    return filter_unique(words)

if __name__ == '__main__':
    sample_text = "Hello, world! Hello, everyone. Welcome to the world of Python."
    print(tokenize_text(sample_text))