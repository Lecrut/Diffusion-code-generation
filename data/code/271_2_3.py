def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalpha())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))