def is_palindrome(s):
    if not s:
        return False
    if len(s) == 1:
        return True
    return s == s[::-1]

if __name__ == '__main__':
    print(is_palindrome("madam"))
    print(is_palindrome(""))
    print(is_palindrome("a"))