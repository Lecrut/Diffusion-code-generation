def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = [
        'racecar',
        'hello',
        'A man a plan a canal Panama',
        'Was it a car or a cat I saw?',
        'No lemon, no melon',
        '',
        'a',
        'ab',
        'aba',
        'abcba',
    ]
    for case in test_cases:
        print(is_palindrome(case.lower().replace(' ', '').replace(',', '').replace('?', '')))