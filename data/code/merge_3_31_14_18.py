import re

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring spaces, punctuation, and case."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a cat and I?",
        "",
        "No 'x' in Nixon"
    ]

    for text in test_cases:
        result = is_palindrome(text)
        print(f"'{text}' -> {result}")