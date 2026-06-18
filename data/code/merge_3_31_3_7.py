import re

def is_palindrome(s: str) -> bool:
    return s == "".join(reversed(filter(lambda c: c.isalnum(), s))) if isinstance(s, str) else False

if __name__ == '__main__':
    print(is_palindrome("A man a plan a canal Panama"))