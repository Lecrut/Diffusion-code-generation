import string

def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome using the two-pointer technique.
    
    This function ignores case and non-alphanumeric characters, comparing only 
    letters and digits from both ends moving towards the center.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Convert to lowercase for case-insensitive comparison
    normalized_s = s.lower()
    
    left, right = 0, len(normalized_s) - 1
    
    while left < right:
        # Move pointers inward skipping non-alphanumeric characters
        if not (normalized_s[left].isalnum()):
            left += 1
            continue
        
        if not (normalized_s[right].isalnum()):
            right -= 1
            continue
            
        # Compare characters at both ends
        if normalized_s[left] != normalized_s[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("hello world", False),
        ("", True),  # Empty string is considered a palindrome
    ]

    for test_string, expected_result in test_cases:
        result = is_palindrome(test_string)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"[{status}] Input: '{test_string}' -> Expected: {expected_result}, Got: {result}")