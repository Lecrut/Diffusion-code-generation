def is_palindrome(s):
    cleaned = ''.join(c for c in s if c.isalnum()).lower()
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("No 'x' in Nixon"))