import re
from collections import Counter

def find_repeated_characters(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    counts = Counter(cleaned_text)
    return sorted([char for char, count in counts.items() if count > 1])

if __name__ == '__main__':
    sample_string = "Hello, World! This is a Test string with repeated characters: 'a', 't', 's'."
    result = find_repeated_characters(sample_string)
    print(result)