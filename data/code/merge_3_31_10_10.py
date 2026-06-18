def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Filter only alphanumeric characters and convert to lowercase in one pass for efficiency
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Use two-pointer approach for O(n) time complexity without extra space beyond input storage
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
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
        ("12321", True),
        ("Hello!", False),
        ("", True),  # Empty string is technically a palindrome
        ("a", True),
    ]

    for test_input, expected_result in test_cases:
        result = is_palindrome(test_input)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"{status}: '{test_input}' -> {result} (Expected: {expected_result})")