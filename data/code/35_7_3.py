def count_vowels(word: str) -> int:
    """Counts the total number of vowels in a given word."""
    vowels = set("aeiouAEIOU")
    return sum(1 for char in word if char in vowels)

if __name__ == '__main__':
    sample_words = ["hello", "world", "beautiful"]

    for test_word in sample_words:
        vowel_count = count_vowels(test_word)
        print(f"Word: {test_word}, Total Vowel Count: {vowel_count}")