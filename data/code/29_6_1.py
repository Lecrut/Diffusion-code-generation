import sys

def reverse_word(word: str) -> str:
    """Reverse a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or command-line arguments
    test_words = ["hello", "python"]

    for w in test_words:
        reversed_w = reverse_word(w)
        print(f"Original: {w}")
        print(f"Reversed: {reversed_w}\n")