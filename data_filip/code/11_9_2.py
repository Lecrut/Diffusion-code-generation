import re
from collections import Counter

def find_repeated_chars(text):
    cleaned = re.sub(r'[^\w]', '', text)
    counts = Counter(cleaned.lower())
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string with some repeated characters: 'a', 'a', 'b', 'b', 'c'."
    result = find_repeated_chars(sample_text)
    print(result)