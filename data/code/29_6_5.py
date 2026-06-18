def reverse_word(word):
    """Returns the reversed version of a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Sample values to run without user input or command-line arguments
    sample_words = ["hello", "world", "Python"]

    for test_word in sample_words:
        reversed_word = reverse_word(test_word)
        print(f"Original: {test_word}")
        print("Reversed:", reversed_word)