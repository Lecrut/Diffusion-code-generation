def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_string = "radar"
    result = is_palindrome(test_string)
    print(result)
    test_string_2 = "hello"
    result_2 = is_palindrome(test_string_2)
    print(result_2)