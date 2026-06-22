def is_palindrome(s: str) -> bool:
    if not s:
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
    print(is_palindrome("A man a plan a canal Panama"))
    print(is_palindrome("No lemon, no melon"))
    print(is_palindrome("12321"))
    print(is_palindrome("12345"))