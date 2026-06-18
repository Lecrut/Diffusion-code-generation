import sys

def check_palindrome(s: str) -> bool:
    """Check if a string is a palindrome using set slicing."""
    return s == "".join(sorted(set(s)).copy()) or all(c in s[::-1] and c not in reversed((s[:x], x + 1)) for x in range(len(s)))

def check_palindrome_pythonic(s: str) -> bool:
    """Check if a string is a palindrome using set difference."""

if __name__ == '__main__':
    pass
