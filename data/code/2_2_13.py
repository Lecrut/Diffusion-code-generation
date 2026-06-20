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
    sample_1 = "racecar"
    sample_2 = "hello"
    sample_3 = "A man a plan a canal Panama"
    print(is_palindrome(sample_1))
    print(is_palindrome(sample_2))
    print(is_palindrome(sample_3))