def is_palindrome(s):
    if len(s) <= 1:
        return True
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(is_palindrome(""))
    print(is_palindrome("a"))
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("abba"))
    print(is_palindrome("abcba"))
    print(is_palindrome("abccba"))
    print(is_palindrome("ab"))
    print(is_palindrome("aa"))