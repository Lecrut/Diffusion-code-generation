def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word."""
    return sum(1 for char in word.lower() if char in 'aeiou')

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file I/O is required.
    test_words = ["hello", "programming", "rhythm"]

    for word in test_words:
        vowel_count = count_vowels(word)
        print(f"Word: {word}, Total Vowel Count: {vowel_count}")