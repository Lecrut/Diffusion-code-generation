def is_palindrome(s):
    normalized_str = ''.join((c.lower() for c in s if c.isalnum()))
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    test_cases = [('', True), ('A man, a plan, a canal: Panama', True), ('race a car', False), (' ', True), ('No lemon, no melon', True), ('!!!', True), ('12321', True), ('123456', False)]
    for s, expected in test_cases:
        result = is_palindrome(s)
        print(f"is_palindrome('{s}') -> {result} (expected: {expected})")