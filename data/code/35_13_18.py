def count_vowels(text: str) -> int:
    """Count vowels (both uppercase and lowercase) in a given string."""
    return sum(1 for char in text if char.lower() in 'aeiou')

if __name__ == '__main__':
    test_strings = [
        "Hello World",
        "AEIOU",
        "Python Programming 2024!",
        "",
        "Rhythm"
    ]

    for s in test_strings:
        print(f'String "{s}" -> Vowel count: {count_vowels(s)}')