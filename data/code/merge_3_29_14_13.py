import sys

def reverse_word(word: str) -> str:
    """Returns the reversed version of a given word."""
    return word[::-1]

if __name__ == '__main__':
    # Sample input to demonstrate functionality without user interaction or CLI args.
    sample_input = "hello"

    try:
        result = reverse_word(sample_input)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)