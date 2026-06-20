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
    test_string_1 = "radar"
    test_string_2 = "hello"
    test_string_3 = "A man a plan a canal Panama".replace(" ", "").lower()
    print(is_palindrome(test_string_1))
    print(is_palindrome(test_string_2))
    print(is_palindrome(test_string_3))