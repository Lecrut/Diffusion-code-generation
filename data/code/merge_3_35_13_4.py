def count_vowels(text: str) -> int:
    """Count vowels (a, e, i, o, u) in a string, case-insensitive."""
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    test_cases = [
        "Hello World",
        "AEIOU",
        "rhythm",
        "",
        "Python Programming"
    ]

    for case in test_cases:
        print(f"'{case}' -> {count_vowels(case)}")