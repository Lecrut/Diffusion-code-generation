def is_palindrome(s):
    cleaned = ''.join((char.lower() for char in s if char.isalnum()))
    return cleaned == cleaned[::-1]
if __name__ == '__main__':
    test_cases = ['', 'A man, a plan, a canal: Panama', 'racecar', 'no lemon, no melon', 'hello', '!@#$%^&*()', 'Was it a car or a cat I saw?']
    for case in test_cases:
        result = is_palindrome(case)
        print(f"'{case}' -> {result}")