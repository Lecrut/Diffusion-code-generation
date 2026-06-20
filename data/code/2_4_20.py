def is_palindrome(s: str) -> bool:
    if not s:
        return True
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "", "a", "abba", "python"]
    results = [is_palindrome(s) for s in test_strings]
    print(results)