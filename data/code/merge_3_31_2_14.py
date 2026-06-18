def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome, ignoring case."""
    return text.lower() == text[::-1]

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "A man a plan a canal Panama"]

    for test_str in sample_strings:
        result = is_palindrome(test_str)
        print(f"Is '{test_str}' a palindrome? {result}")