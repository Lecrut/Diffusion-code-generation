def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    sample_strings = [
        "racecar",
        "hello",
        "a",
        "ab",
        "madam",
        "Python",
        ""
    ]
    for s in sample_strings:
        result = is_palindrome(s)
        print(f"{s}: {result}")