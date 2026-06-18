def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring case."""
    cleaned = s.lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "Hello, World!", "Python"]
    for word in test_cases:
        print(f"'{word}': {is_palindrome(word)}")