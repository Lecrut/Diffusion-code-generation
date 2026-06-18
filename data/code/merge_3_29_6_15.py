def reverse_word(word):
    """Returns the reversed version of a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    test_words = ["hello", "world", "Python"]

    for word in test_words:
        print(f"Original: {word}")
        reversed_word = reverse_word(word)
        print(f"Reversed: {reversed_word}")