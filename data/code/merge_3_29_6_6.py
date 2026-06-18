import sys

def reverse_word(word: str) -> str:
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to satisfy requirements without user interaction.
    test_words = ["hello", "world"]

    for word in test_words:
        print(reverse_word(word))