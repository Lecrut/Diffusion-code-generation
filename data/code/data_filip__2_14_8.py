def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    result = is_palindrome("racecar")
    print(result)
    result2 = is_palindrome("hello")
    print(result2)