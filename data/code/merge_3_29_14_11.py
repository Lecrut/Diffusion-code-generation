def reverse_word(word: str) -> str:
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input.
    test_cases = ["hello", "Python", "world"]

    for word in test_cases:
        print(f"Original: {word}")
        reversed_word = reverse_word(word)
        print(f"Reversed: {reversed_word}\n")