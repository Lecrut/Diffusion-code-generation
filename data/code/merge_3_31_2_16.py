def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case."""
    return s.lower() == s[::-1]

if __name__ == '__main__':
    # Sample test cases without user input or command-line arguments.
    sample_strings = ["racecar", "hello", "A man a plan a canal Panama"]

    for text in sample_strings:
        result = is_palindrome(text)
        print(f"'{text}' is {'a' if result else 'not'} a palindrome.")