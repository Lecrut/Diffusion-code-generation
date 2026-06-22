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
    samples = [
        'racecar',
        'hello',
        'madam',
        'python',
        '',
        'a',
        'abba',
        'abcba',
        'abcd',
        'A man a plan a canal Panama'.replace(' ', '').lower(),
    ]
    for sample in samples:
        print(is_palindrome(sample))