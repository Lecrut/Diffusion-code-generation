def is_palindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("No 'x' in Nixon"))
    print(is_palindrome(""))