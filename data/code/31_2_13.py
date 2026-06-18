def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case."""
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input
    test_strings = ["racecar", "hello", "A man a plan a canal Panama"]

    for word in test_strings:
        result = is_palindrome(word)
        print(f"'{word}' -> {result}")