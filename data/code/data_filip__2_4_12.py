def is_palindrome(text: str) -> bool:
    if not text:
        return True
    if len(text) == 1:
        return True
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))
    print(is_palindrome(""))
    print(is_palindrome("a"))