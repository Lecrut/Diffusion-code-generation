def count_vowels(word: str) -> int:
    """Returns the total number of vowels in the given word."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    test_words = ["hello", "python", "raining"]

    for sample_word in test_words:
        total_count = count_vowels(sample_word)
        print(f"Word: {sample_word} -> Total vowels: {total_count}")