import sys

def reverse_word(word):
    """Returns the reversed version of the input word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user interaction or external dependencies are required
    test_cases = ["hello", "python"]

    for word in test_cases:
        print(f"Original: {word}")
        reversed_word = reverse_word(word)
        print(f"Reversed: {reversed_word}")