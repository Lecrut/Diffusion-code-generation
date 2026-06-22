def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["radar", "hello", "level", "python"]
    for case in test_cases:
        print(is_palindrome(case))