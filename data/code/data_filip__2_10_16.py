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
    test_cases = ["racecar", "hello", "A man a plan a canal Panama", "12321", "12345"]
    for test in test_cases:
        print(is_palindrome(test))