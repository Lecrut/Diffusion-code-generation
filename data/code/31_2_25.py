def is_palindrome(s):
    return s.lower() == s[::-1].lower()

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "Level", "world"]
    for test in test_strings:
        result = is_palindrome(test)
        print(f"'{test}' is a palindrome: {result}")