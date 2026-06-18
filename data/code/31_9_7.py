def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring case."""
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "Hello, World!", "Python"]
    for word in test_cases:
        print(f"'{word}' is {'a' if is_palindrome(word) else 'not'} a palindrome")