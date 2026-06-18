import sys

def reverse_word(text: str) -> str:
    """Return a new string with characters in reversed order."""
    return text[::-1]

if __name__ == '__main__':
    # Sample values to demonstrate functionality without user input or file access.
    sample_input = "Hello World"
    output_text = reverse_word(sample_input)

    print(f"'{sample_input}'")