def reverse_word(word):
    """Returns the reversed version of a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access
    test_cases = ["hello", "Python", "World"]

    for test_word in test_cases:
        reversed_word = reverse_word(test_word)
        print(f"Original word: {test_word}")
        print(f"Reversed word:  {reversed_word}\n")