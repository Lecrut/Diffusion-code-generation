def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = ["A man a plan a canal Panama", "racecar", "hello"]
    for case in test_cases:
        result = is_palindrome(case)
        print(f"'{case}' is a palindrome: {result}")