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
    test_strings = ["racecar", "hello", "madam", "a", ""]
    results = [is_palindrome(s) for s in test_strings]
    for string, result in zip(test_strings, results):
        print(f"{string}: {result}")