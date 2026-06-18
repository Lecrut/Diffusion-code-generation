def is_palindrome_two_pointers(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.
    
    This function compares characters from both ends of the string moving towards the center,
    ignoring non-alphanumeric characters and case sensitivity as per standard palindrome definition.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) as no extra data structures are used beyond pointers.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move left pointer to next alphanumeric character
        if not s[left].isalnum():
            left += 1
            continue
        
        # Move right pointer to previous alphanumeric character
        if not s[right].isalnum():
            right -= 1
            continue
            
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("Hello World!", False),
        ("", True),  # Empty string is technically a palindrome
        ("a", True)   # Single character is always a palindrome
    ]

    for test_input, expected_result in samples:
        result = is_palindrome_two_pointers(test_input)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"[{status}] Input: '{test_input}' -> Expected: {expected_result}, Got: {result}")