import re
from collections import Counter

def find_repeated_characters(text):
    cleaned = re.sub(r'[^\w]', '', text.lower())
    cleaned = cleaned.replace(' ', '')
    counts = Counter(cleaned)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string with some repeated letters."
    result = find_repeated_characters(sample_text)
    print(result)