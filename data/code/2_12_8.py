def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("Was it a car or a cat I saw?"))
    print(is_palindrome("No 'x' in Nixon"))