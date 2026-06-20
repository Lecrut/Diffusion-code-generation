def is_palindrome(s):
    return all(c == d for c, d in zip(s, reversed(s)))

if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("a"))
    print(is_palindrome(""))
    print(is_palindrome("abba"))