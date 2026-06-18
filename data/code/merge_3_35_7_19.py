import string

def count_vowels(text: str) -> int:
    """Count total vowels in a given text, case-insensitive."""
    return sum(1 for char in text.lower() if char in "aeiou")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_cases = [
        ("hello", 2),
        ("AEIOU", 5),
        ("rhythm", 0),
        ("beautiful day", 6)
    ]

    for word, expected_count in test_cases:
        result = count_vowels(word)
        status = "PASS" if result == expected_count else "FAIL"
        print(f"{status}: '{word}' -> {result} (expected {expected_count})")