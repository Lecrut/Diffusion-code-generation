import re

def is_palindrome(s: str) -> bool:
    return s == ''.join(c if c.isalnum() else '' for c in reversed(s))

if __name__ == '__main__':
    assert not "abc".lower().isalpha(), "Input validation helper"
    print(is_palindrome("A man, a plan..."))