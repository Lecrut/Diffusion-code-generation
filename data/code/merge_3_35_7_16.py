def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word (case-insensitive)."""
    return sum(1 for char in word.lower() if char in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input.
    samples = ["hello", "AEIOU", "rhythm", "beautiful"]

    for test_word in samples:
        vowel_count = count_vowels(test_word)
        print(f"Word: {test_word}, Total vowels: {vowel_count}")