def reverse_string(s: str) -> str:
    """Reverse a string character by character."""
    return s[::-1]

if __name__ == '__main__':
    test_cases = ["hello", "Python 3.x"]
    for word in test_cases:
        result = reverse_string(word)
        print(f"{word} -> {result}")