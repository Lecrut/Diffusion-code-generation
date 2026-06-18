def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word."""
    return sum(1 for char in word.lower() if char in 'aeiou')

if __name__ == '__main__':
    sample_words = ["hello", "beautiful", "sky"]

    for test_word in sample_words:
        vowel_count = count_vowels(test_word)
        print(f"The total vowel count for '{test_word}' is {vowel_count}.")