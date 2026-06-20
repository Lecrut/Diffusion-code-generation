def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    n = len(cleaned)
    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome(""))
    print(is_palindrome("Madam"))