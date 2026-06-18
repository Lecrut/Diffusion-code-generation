def reverse_string(text: str) -> str:
    """Returns a new string with characters in reversed order."""
    return text[::-1]

if __name__ == '__main__':
    sample_value = "Hello, World!"
    print(reverse_string(sample_value))