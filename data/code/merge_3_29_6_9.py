def reverse_word(word):
    """Returns the reversed version of a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    sample_words = ["hello", "world", "python"]

    for test_word in sample_words:
        reversed_word = reverse_word(test_word)
        print(reversed_word)