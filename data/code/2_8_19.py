def is_palindrome(s):
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    return normalized == normalized[::-1]

if __name__ == '__main__':
    test_cases = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat I saw?", "12321", "hello"]
    for case in test_cases:
        print(is_palindrome(case))