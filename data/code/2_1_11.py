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
    test_strings = ['racecar', 'hello', 'a', 'abba', 'abcde', 'madam', '12321']
    results = []
    for test in test_strings:
        result = is_palindrome(test)
        results.append(result)
    print(results)