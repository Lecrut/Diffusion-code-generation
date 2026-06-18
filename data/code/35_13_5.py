def count_vowels(text: str) -> int:
    """Count total number of vowels (a, e, i, o, u) in a string, case-insensitive."""
    return sum(1 for char in text.lower() if char in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    samples = [
        "Hello World",          # Expected: 3 (e, o, o)
        "AEIOU aeiou AaEiOu",   # Expected: 12
        "bcdfg hklmnpq rstuvwxy z", # Expected: 0
        "",                     # Expected: 0
    ]

    for sample in samples:
        result = count_vowels(sample)
        print(f"Input: '{sample}' -> Vowel Count: {result}")