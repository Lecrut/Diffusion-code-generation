import collections
import string

def find_repeated_characters(text: str) -> list[str]:
    punctuation = set(string.punctuation)
    cleaned_chars = [char.lower() for char in text if char.isalnum()]
    counts = collections.Counter(cleaned_chars)
    repeated = [char for char, count in counts.items() if count > 1]
    repeated.sort()
    return repeated

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string with some repeated characters."
    result = find_repeated_characters(sample_text)
    print(result)