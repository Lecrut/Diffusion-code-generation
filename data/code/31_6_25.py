def is_palindrome(s):
    normalized = ''.join((c.lower() for c in s if c.isalnum()))
    return normalized == normalized[::-1]
if __name__ == '__main__':
    test_cases = ['', 'A man, a plan, a canal: Panama', 'racecar', 'no lemon, no melon', '!!!', 'Not a palindrome', 'Was it a car or a cat I saw?']
    for test in test_cases:
        result = is_palindrome(test)
        print(f"'{test}': {result}")