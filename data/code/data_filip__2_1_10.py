def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    result1 = is_palindrome("racecar")
    result2 = is_palindrome("hello")
    print(result1)
    print(result2)