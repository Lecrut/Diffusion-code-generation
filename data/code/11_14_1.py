import sys
from collections import Counter

def detect_duplicate_characters(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    frequency_map = Counter(text)
    duplicates = {char: count for char, count in frequency_map.items() if count > 1}
    return duplicates

if __name__ == "__main__":
    sample_text = "professional-grade Python module that detects character frequency duplicates"
    result = detect_duplicate_characters(sample_text)
    print(result)