def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == '__main__':
    test_strings = ["A man a plan a canal Panama", "racecar", "hello"]
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' is a palindrome: {result}")