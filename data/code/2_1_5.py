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
    test_cases = ['racecar', 'hello', 'A man a plan a canal Panama'.replace(' ', '').lower(), 'madam', 'python', 'abcba', '', 'a']
    for test in test_cases:
        result = is_palindrome(test)
        print(f"is_palindrome('{test}') = {result}")