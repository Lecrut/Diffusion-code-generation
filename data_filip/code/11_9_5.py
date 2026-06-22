import re
from collections import Counter

def find_repeated_characters(text: str) -> list:
    cleaned = re.sub(r'[\s\W_]+', '', text)
    cleaned = cleaned.lower()
    counts = Counter(cleaned)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test. Python is great."
    result = find_repeated_characters(sample_text)
    print(result)