def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "level", "world", "madam"]
    for test in test_strings:
        print(is_palindrome(test))