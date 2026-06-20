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
    test_strings = ["racecar", "hello", "A man a plan a canal Panama", "Madam"]
    results = [(s, is_palindrome(s)) for s in test_strings]
    for s, is_pal in results:
        print(f"'{s}': {is_pal}")