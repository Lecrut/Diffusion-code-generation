import sys

def reverse_word(word: str) -> str:
    """Reverse a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input.
    test_words = ["hello", "python", "world"]

    for w in test_words:
        reversed_w = reverse_word(w)
        print(f"Original word: {w}")
        print(f"Reversed word:  {reversed_w}\n")