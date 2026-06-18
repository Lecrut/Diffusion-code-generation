def reverse_string(s: str) -> str:
    """Reverse a given ASCII string in-place using slice notation."""
    return s[::-1]

if __name__ == '__main__':
    sample = "Hello, World!"
    result = reverse_string(sample)
    print(result)