def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_strings = ["radar", "hello", "level", "world"]
    for string in test_strings:
        print(f"'{string}' is a palindrome: {is_palindrome(string)}")