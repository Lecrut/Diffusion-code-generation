def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome("a"))
    print(is_palindrome("abba"))
    print(is_palindrome("abcba"))
    print(is_palindrome("ab"))