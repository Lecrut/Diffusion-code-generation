def count_vowels(text: str) -> int:
    """Count total number of vowels (a, e, i, o, u) in a string case-insensitively."""
    vowels = set("aeiou")
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or arguments.
    test_cases = [
        "Hello, World!",  # Expected: 2 (e, o)
        "AEIOU",          # Expected: 5
        "Python Programming",  # Expected: 4 (y is not counted here based on strict aeiou definition)
        "",               # Expected: 0
    ]

    for test_string in test_cases:
        result = count_vowels(test_string)
        print(f"Input: '{test_string}' -> Vowel Count: {result}")