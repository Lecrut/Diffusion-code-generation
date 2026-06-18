def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome using built-in methods."""
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "A man, a plan, a canal: Panama"]