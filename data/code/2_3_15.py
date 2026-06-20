def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["radar", "hello", "Aibohphobia", "Python"]
    for case in test_cases:
        result = is_palindrome(case)
        print(result)