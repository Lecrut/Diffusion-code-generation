def reverse_string(s: str) -> str:
    """Reverses a string by slicing it backwards."""
    return s[::-1]

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = reverse_string(sample_input)
    print(result)