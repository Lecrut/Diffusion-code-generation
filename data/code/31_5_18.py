def is_palindrome_two_pointers(s: str) -> bool:
    """
    Checks if a given string is a palindrome using the two-pointer technique.
    
    The function compares characters from both ends moving towards the center,
    skipping non-alphanumeric characters and case differences to ensure accuracy.
    
    Time Complexity: O(n) where n is the length of the input string.
    Space Complexity: O(1) as no extra data structures are used beyond pointers.

    Args:
        s (str): The input string to check for palindrome property.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome_two_pointers("A man, a plan, a canal: Panama")
        True
        
        >>> is_palindrome_two_pointers("race a car")
        False
    
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Move left pointer forward if current character is not alphanumeric
        if not s[left].isalnum():
            left += 1
            continue
        
        # Move right pointer backward if current character is not alphanumeric
        if not s[right].isalnum():
            right -= 1
            continue

        # Compare characters (case-insensitive) and move both pointers inward
        char_diff = ord(s[left]).lower() - ord(s[right]).lower()
        if char_diff != 0:
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files

    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a cat I saw?", True),
        ("no 'x' in Nixon", True),
        ("hello world!", False),
        ("", True),  # Empty string is technically a palindrome
        ("a", True),  # Single character is always a palindrome
    ]

    for i, (input_string, expected_result) in enumerate(test_cases):
        result = is_palindrome_two_pointers(input_string)
        
        if result == expected_result:
            print(f"Test Case {i + 1}: PASSED")
        else:
            print(f"Test Case {i + 1}: FAILED (Expected {expected_result}, Got {result})")

    # Demonstration with a custom input in the main block to show functionality directly
    sample_input = "No 'x' in Nixon"
    result_sample = is_palindrome_two_pointers(sample_input)
    
    print(f"\nSample Test: '{sample_input}'")
    if result_sample == True:
        status = "Result: Is Palindrome (True)"
    else:
        status = "Result: Not a Palindrome (False)"
        
    # Ensure correctness for the specific sample mentioned earlier in comments
    
    print(status)