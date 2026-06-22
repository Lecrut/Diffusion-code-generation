def is_palindrome(s):
    length = len(s)
    half = length // 2
    for i in range(half):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("a"))
    print(is_palindrome("abba"))
    print(is_palindrome("abcde"))