def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_values = ["radar", "hello", "level", "python"]
    for value in test_values:
        print(is_palindrome(value))