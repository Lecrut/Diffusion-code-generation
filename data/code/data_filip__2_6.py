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
    test_strings = ["radar", "hello", "racecar", "python", "noon"]
    for text in test_strings:
        print(is_palindrome(text))