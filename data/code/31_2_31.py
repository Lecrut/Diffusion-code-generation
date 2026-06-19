def is_palindrome(s):
    return s == s[::-1]

if __name__ == '__main__':
    test_string = "radar"
    result = is_palindrome(test_string)
    print(result)