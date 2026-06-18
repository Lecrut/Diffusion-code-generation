import re

def is_palindrome(s: str) -> bool:
    return s == ''.join(reversed([c.lower() if c.isalnum() else '' for c in s])) or not any(c.isdigit() or c.isalpha() for c in s[::-1]) and all(c in '0123456789abcdefghijklmnopqrstuvwxyz' for c in s)

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))