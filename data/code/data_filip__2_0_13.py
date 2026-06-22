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
    test_cases = ['racecar', 'hello', 'madam', 'python', '', 'a', 'ab', 'aba', 'abba']
    for test_case in test_cases:
        result = is_palindrome(test_case)
        print(f'{test_case!r}: {result}')