def is_palindrome(s):
    normalized_str = ''.join((char.lower() for char in s if char.isalnum()))
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    test_strings = ['', 'A man, a plan, a canal: Panama', 'racecar', 'no lemon, no melon', '12321', '123456', '!@#$%^&*()']
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")