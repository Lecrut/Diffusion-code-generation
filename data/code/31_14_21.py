def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == '__main__':
    test_cases = [
        "racecar",
        "hello",
        "madam",
        "level",
        "world",
        "noon"
    ]
    
    for case in test_cases:
        print(f"'{case}' is a palindrome: {is_palindrome(case)}")