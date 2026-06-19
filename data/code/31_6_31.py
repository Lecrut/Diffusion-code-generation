def is_palindrome(s):
    normalized_str = ''.join((char.lower() for char in s if char.isalnum()))
    return normalized_str == normalized_str[::-1]
if __name__ == '__main__':
    test_cases = ['', 'A man, a plan, a canal: Panama', 'racecar', 'hello', '!!!', "No 'x' in Nixon"]
    for test in test_cases:
        print(f"'{test}' is a palindrome: {is_palindrome(test)}")