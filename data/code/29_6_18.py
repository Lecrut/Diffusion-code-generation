def reverse_word(word: str) -> str:
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Sample values instead of user prompts to ensure no interactive input is required.
    sample_words = ["hello", "python"]

    for word in sample_words:
        print(reverse_word(word))