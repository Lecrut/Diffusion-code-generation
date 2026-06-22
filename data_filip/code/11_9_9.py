import string
from collections import Counter

def find_repeated_chars(s):
    cleaned = (c.lower() for c in s if c.isalnum())
    counts = Counter(cleaned)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test."
    result = find_repeated_chars(sample_text)
    print(result)