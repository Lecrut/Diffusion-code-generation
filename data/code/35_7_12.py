def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word."""
    return sum(1 for char in word.lower() if char in 'aeiou')

if __name__ == '__main__':
    sample_word = "hello"
    vowel_count = count_vowels(sample_word)
    print(f"The word '{sample_word}' has {vowel_count} vowels.")