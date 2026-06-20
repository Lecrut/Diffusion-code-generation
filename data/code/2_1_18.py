def is_palindrome(s: str) -> bool:
    length = len(s)
    if length <= 1:
        return True
    left = 0
    right = length - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_strings = [
        "racecar",
        "hello",
        "madam",
        "a",
        "ab",
        "abcba",
        "12321",
        "python",
        "No 'x' in Nixon",
        ""
    ]
    for s in test_strings:
        result = is_palindrome(s)
        print(result)