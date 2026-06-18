def count_vowels(text):
    """Count vowels (a, e, i, o, u) in a string, case-insensitive."""
    return len([c for c in text if c.lower() in 'aeiou'])

if __name__ == '__main__':
    samples = [
        "Hello World",
        "AEIOU aeiou",
        "Python Programming 2024"
    ]

    for test_str in samples:
        print(f"'{test_str}' -> {count_vowels(test_str)} vowels")