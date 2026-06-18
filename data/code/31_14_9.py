import re

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring spaces, punctuation, and case."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race car",
        "Hello, World!",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "Not a palindrome"
    ]

    for test_str in test_cases:
        result = is_palindrome(test_str)
        print(f"'{test_str}' -> {result}")