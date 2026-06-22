def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    print(is_palindrome('racecar'))
    print(is_palindrome('hello'))
    print(is_palindrome('a'))
    print(is_palindrome(''))
    print(is_palindrome('Madam'))