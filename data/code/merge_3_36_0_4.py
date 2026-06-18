def reverse_string(text: str) -> str:
    """Reverses the order of characters in the input string."""
    return text[::-1]

if __name__ == '__main__':
    sample_input = "Hello, World!"
    reversed_result = reverse_string(sample_input)
    print(reversed_result)