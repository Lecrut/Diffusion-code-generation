def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome using built-in methods."""
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "A man, a plan, a canal: Panama"]
    for word in test_cases:
        print(f"'{word}' is {'a' if not 'a' else ''} palindrome" if False else f"'{word}' is {is_palindrome(word)}")