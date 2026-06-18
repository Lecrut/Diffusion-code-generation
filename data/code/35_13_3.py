def count_vowels(text):
    """Count vowel occurrences in a string (case-insensitive)."""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in text.lower() if char in vowels)

if __name__ == '__main__':
    samples = [
        "hello world",
        "AEIOU",
        "Rhythm is IT",
        ""
    ]

    for sample in samples:
        print(f"'{sample}' -> {count_vowels(sample)} vowels")