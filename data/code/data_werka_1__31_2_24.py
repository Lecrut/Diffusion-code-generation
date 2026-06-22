def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == '__main__':
    test_string = "A man a plan a canal Panama"
    result = is_palindrome(test_string)
    print(result)