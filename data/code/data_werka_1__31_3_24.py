def is_palindrome(s):
    return s == s[::-1]
if __name__ == '__main__':
    print(is_palindrome('racecar'))
    print(is_palindrome('hello'))
    print(is_palindrome('madam'))
    print(is_palindrome('level'))
    print(is_palindrome('world'))