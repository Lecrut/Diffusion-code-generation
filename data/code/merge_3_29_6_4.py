def reverse_word(word):
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction is required
    sample_words = ["hello", "world"]
    
    for test_word in sample_words:
        print(f"Original: {test_word}")
        reversed_word = reverse_word(test_word)
        print(f"Reversed: {reversed_word}")