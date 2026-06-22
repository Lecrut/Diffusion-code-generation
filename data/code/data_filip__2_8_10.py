import re

def is_palindrome(s):
    normalized = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return normalized == normalized[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))
    print(is_palindrome("Was it a car or a cat I saw?"))
    print(is_palindrome("No 'x' in Nixon"))
    print(is_palindrome("hello"))