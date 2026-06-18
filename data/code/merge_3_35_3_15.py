from typing import List

def count_vowels(text: str) -> int:
    """Count vowels in a string, case-insensitive."""
    return sum(c.lower() in 'aeiou' for c in text)

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "AEIOU" * 10,
        "",
        "Rhythm is soft!"
    ]
    print(f"The vowel count for {sample_strings} are: {[count_vowels(s) for s in sample_strings]}")