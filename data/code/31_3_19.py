def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("abba", True),
        ("python", False)
    ]
    for string, expected in test_cases:
        result = is_palindrome(string)
        assert result == expected, f"Failed for '{string}': got {result}, expected {expected}"