def is_palindrome(text):
    return text == text[::-1]

if __name__ == '__main__':
    test_cases = ["racecar", "hello", "madam", "world", ""]
    for case in test_cases:
        print(is_palindrome(case))