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
    test_strings = ["racecar", "hello", "madam", "a"]
    for s in test_strings:
        print(f"{s}: {is_palindrome(s)}")