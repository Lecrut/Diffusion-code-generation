from collections import Counter

def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring spaces and punctuation."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())

if __name__ == '__main__':
    pass
