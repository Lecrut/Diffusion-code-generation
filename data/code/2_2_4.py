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
    sample_strings = ["racecar", "hello", "A man a plan a canal Panama", "madam"]
    for s in sample_strings:
        print(is_palindrome(s))