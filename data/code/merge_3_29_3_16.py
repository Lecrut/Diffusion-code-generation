def reverse_string(s: str) -> str:
    """Reverse a given ASCII string."""
    return s[::-1]

if __name__ == '__main__':
    sample_input = "Hello, World!"
    print(reverse_string(sample_input))