from typing import List

def count_vowels(text: str) -> int:
    """Return the number of vowels in a case-insensitive manner."""
    return sum(1 for char in text if char.lower() in "aeiou")

if __name__ == '__main__':
    samples = ["Hello World", "AEIOU", "", "Python3.9"]
    for sample in samples:
        print(f"'{sample}': {count_vowels(sample)} vowels")