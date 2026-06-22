def is_palindrome(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    def validate_string(s):
        return len(s) > 0
    
    if not validate_string(s):
        return False

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
        "noon",
        "",
        "a",
        "ab"
    ]
    for case in test_cases:
        print(f"'{case}' is a palindrome: {is_palindrome(case)}")