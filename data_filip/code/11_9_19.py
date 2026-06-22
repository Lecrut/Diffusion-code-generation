import string
from collections import Counter

def find_repeated_characters(text):
    cleaned_text = [char.lower() for char in text if char not in string.whitespace and char not in string.punctuation]
    counts = Counter(cleaned_text)
    return sorted([char for char, count in counts.items() if count > 1])

if __name__ == '__main__':
    sample_text = "Hello, World!  World... H-hello!!"
    result = find_repeated_characters(sample_text)
    print(result)