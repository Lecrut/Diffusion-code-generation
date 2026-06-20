def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    test_string_1 = "radar"
    test_string_2 = "hello"
    test_string_3 = "A"
    print(is_palindrome(test_string_1))
    print(is_palindrome(test_string_2))
    print(is_palindrome(test_string_3))