def reverse_string(s: str) -> str:
    """Reverse a string character by character."""
    return s[::-1]

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = reverse_string(sample_input)
    print(result)