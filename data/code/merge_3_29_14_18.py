def reverse_word(word):
    """Returns the reversed version of the given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access
    test_cases = ["hello", "Python", "World"]

    for word in test_cases:
        print(f"Original: {word}")
        reversed_word = reverse_word(word)
        print(f"Reversed: {reversed_word}\n")