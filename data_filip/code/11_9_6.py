import re
from collections import Counter

def find_repeated_chars(text):
    cleaned = re.sub(r'\W', '', text).lower()
    counts = Counter(cleaned)
    return [char for char, count in counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "Hello, World!   This is a test string with repeated characters: aaaa, bbbb, ccc."
    result = find_repeated_chars(sample_text)
    print(result)