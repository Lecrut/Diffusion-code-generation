import sys

def reverse_word(word: str) -> str:
    """Reverse a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or network access.
    test_cases = ["hello", "Python"]

    for case in test_cases:
        reversed_case = reverse_word(case)
        print(reversed_case)