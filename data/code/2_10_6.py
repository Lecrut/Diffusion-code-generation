def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_string_1 = "racecar"
    test_string_2 = "hello"
    test_string_3 = "A man a plan a canal Panama"
    result_1 = is_palindrome(test_string_1)
    result_2 = is_palindrome(test_string_2)
    result_3 = is_palindrome(test_string_3)
    print(result_1)
    print(result_2)
    print(result_3)