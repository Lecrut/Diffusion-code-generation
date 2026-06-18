import re

def is_palindrome(s: str) -> bool:
    """Check if a string reads the same forwards and backward, ignoring spaces/punctuation."""
    cleaned = ''.join(c.lower() for c in s.replace(' ', ''))
    
    # Palindromic check using two pointers (O(n) time)
    return is_palindrome_two_pointers(cleaned)

def is_palindrome_two_pointers(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Test cases with hard-coded values (no user input or files)
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race car",
        "No 'x' in Nixon",
        "Madam",
        "Hello World!",
        "abc",
        ""
    ]
    
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' -> {result}")