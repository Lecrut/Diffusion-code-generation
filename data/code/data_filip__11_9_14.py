import string
from collections import Counter

def find_repeated_characters(text):
    cleaned = []
    for char in text:
        if not char.isspace() and char not in string.punctuation:
            cleaned.append(char)
    counts = Counter(cleaned)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string with some repeated words."
    result = find_repeated_characters(sample_text)
    print(result)