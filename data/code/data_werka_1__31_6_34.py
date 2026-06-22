def is_palindrome(s):
    normalized_str = ''.join((char.lower() for char in s if char.isalnum()))
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    test_cases = ['', 'A man, a plan, a canal: Panama', 'racecar', 'No lemon, no melon', '!!!', '12321', 'Was it a car or a cat I saw?']
    for case in test_cases:
        print(f"'{case}' is a palindrome: {is_palindrome(case)}")