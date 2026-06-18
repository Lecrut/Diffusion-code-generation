def count_vowels(text: str) -> int:
    """Count total number of vowels in the input string using a single loop."""
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    test_cases = [
        "Hello World",      # Expected: 3 (e, o, o)
        "AEIOU aeiou",     # Expected: 10
        "Python programming", # Expected: 4 (o, i, u, i)
        ""                 # Expected: 0
    ]

    for sample in test_cases:
        result = count_vowels(sample)
        print(f"'{sample}' -> {result}")