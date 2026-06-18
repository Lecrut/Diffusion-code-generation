def count_vowels(text: str) -> int:
    """Counts the total number of vowels (a, e, i, o, u) in a string."""
    text = text.lower()
    return sum(1 for char in text if char in 'aeiou')

if __name__ == '__main__':
    sample_word = "hello"
    vowel_count = count_vowels(sample_word)
    print(f"The word '{sample_word}' has {vowel_count} vowels.")