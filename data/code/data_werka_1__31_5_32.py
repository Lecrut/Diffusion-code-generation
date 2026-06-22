def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    sample_values = [
        "racecar",
        "hello",
        "madam",
        "level",
        "world"
    ]
    
    for value in sample_values:
        print(is_palindrome(value))