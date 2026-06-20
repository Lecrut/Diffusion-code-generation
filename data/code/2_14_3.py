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
    test_cases = ["radar", "hello", "A", "racecar", "noon", "python"]
    for text in test_cases:
        result = is_palindrome(text)
        print(f"{text}: {result}")