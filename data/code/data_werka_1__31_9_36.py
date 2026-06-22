def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_string = "radar"
    print(is_palindrome(test_string))