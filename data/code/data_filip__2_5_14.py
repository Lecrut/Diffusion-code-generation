def is_palindrome(s):
    cleaned = s.lower()
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_cases = ["Racecar", "Hello", "A man a plan a canal Panama", "No"]
    for case in test_cases:
        print(case, is_palindrome(case))