def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word, case-insensitive."""
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in word.lower() if char in vowel_set)

if __name__ == '__main__':
    sample_words = ["hello", "aeiou", "rhythm"]
    
    # Simulate prompting by iterating through hard-coded samples
    for test_word in sample_words:
        count = count_vowels(test_word)
        print(f"The word '{test_word}' has {count} vowel(s).")