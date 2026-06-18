from typing import List

def count_vowels(text: str) -> int:
    """Count vowels in a string case-insensitively."""
    return sum(1 for char in text if char.lower() in {'a', 'e', 'i', 'o', 'u'})

if __name__ == '__main__':
    sample_strings = ["Hello", "AEIOU", "rhythm", "aeiou"]
    results: List[int] = [count_vowels(s) for s in sample_strings]
    print(results)  # Expected output: [3, 5, 0, 5]