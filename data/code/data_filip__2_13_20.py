def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_values = ["racecar", "hello", "madam", "world", "A", "12321", "12345"]
    for value in test_values:
        print(f"{value}: {is_palindrome(value)}")