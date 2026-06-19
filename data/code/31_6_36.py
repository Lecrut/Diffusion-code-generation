def is_palindrome(s):
    normalized_str = ''.join((char.lower() for char in s if char.isalnum()))
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    test_cases = ['', 'A man, a plan, a canal: Panama', 'racecar', 'no lemon, no melon', '!!!', 'Was it a car or a cat I saw?', 'Not a palindrome']
    for case in test_cases:
        result = is_palindrome(case)
        print(f"'{case}' -> {result}")