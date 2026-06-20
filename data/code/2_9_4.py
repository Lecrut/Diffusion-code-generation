def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    return s == s[::-1]

if __name__ == '__main__':
    try:
        print(is_palindrome("racecar"))
        print(is_palindrome("hello"))
        print(is_palindrome("madam"))
        print(is_palindrome(123))
    except TypeError as e:
        print(e)