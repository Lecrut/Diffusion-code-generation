def is_palindrome(s: str) -> bool:
    s = s.lower()
    left = 0
    right = len(s) - 1
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
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "No 'x' in Nixon",
        "madam",
        "python"
    ]

    for s in test_strings:
        result = is_palindrome(s)
        print(f"{s!r}: {result}")