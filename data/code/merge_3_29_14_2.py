def reverse_word(word):
    """Return the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction is required at runtime.
    sample_words = ["hello", "Python", "world"]

    for test_word in sample_words:
        reversed_word = reverse_word(test_word)
        print(f"Original word: {test_word}")
        print(f"Reversed word: {reversed_word}\n")