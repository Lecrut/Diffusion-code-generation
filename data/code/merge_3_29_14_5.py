def reverse_word(word: str) -> str:
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user interaction.
    test_cases = ["hello", "world", "python"]

    for test_word in test_cases:
        print(f"Original: {test_word}")
        reversed_word = reverse_word(test_word)
        print(f"Reversed: {reversed_word}\n")