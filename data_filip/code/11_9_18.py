import re
from collections import Counter

def find_repeated_characters(text: str) -> list:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    counts = Counter(cleaned)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string."
    result = find_repeated_characters(sample_text)
    print(result)