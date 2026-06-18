import sys

def reverse_word(word: str) -> str:
    """Returns the reversed version of the given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or interactive prompts are required.
    test_cases = ["hello", "python", "world"]

    for word in test_cases:
        reversed_word = reverse_word(word)
        print(reversed_word)