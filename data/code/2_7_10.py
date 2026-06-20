def is_palindrome(s):
    return all(a == b for a, b in zip(s, reversed(s)))

if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("madam"))
    print(is_palindrome("python"))