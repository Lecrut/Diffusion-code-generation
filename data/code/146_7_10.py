def is_palindrome(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    test_strings = ["radar", "python", "level", "world"]
    results = [is_palindrome(s) for s in test_strings]
    print(results)