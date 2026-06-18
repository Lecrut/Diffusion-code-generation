"""
Optimized Palindrome Checker Module

This module provides two alternative implementations to check if a string is a palindrome:
1. Two-pointer approach (efficient in terms of space complexity)
2. String slicing approach (simple and pythonic, efficient for typical use cases)

Both methods are case-insensitive and ignore non-alphanumeric characters.
"""

def is_palindrome_two_pointer(s: str) -> bool:
    """
    Check if the string is a palindrome using two pointers.
    
    Args:
        s (str): Input string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Filter and prepare clean input
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
        
    return True

def is_palindrome_slicing(s: str) -> bool:
    """
    Check if the string is a palindrome using string slicing.
    
    Args:
        s (str): Input string to check
        
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Filter and prepare clean input for comparison
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    return cleaned == reversed(cleaned)

if __name__ == '__main__':
    # Hard-coded sample values to test both implementations
    
    samples = [
        "A man, a plan, a canal: Panama",  # True case with special characters and spaces
        "race a car",                      # False case (simple words)
        "",                               # Edge case: empty string
        "Was it a cat I saw?",            # Another complex punctuation example
        "Madam",                          # Classic palindrome without non-alnum chars
    ]
    
    print("Palindrome Checker Results\n")
    print("-" * 50)
    
    for sample in samples:
        result_two = is_palindrome_two_pointer(sample)
        result_slice = is_palindrome_slicing(sample)
        
        # Verify both methods give same results
        assert result_two == result_slice, "Implementation discrepancy detected!"
        
        status = "✓ Palindrome" if result_two else "✗ Not a palindrome"
        print(f"Input: '{sample}'")
        print(f"Two-pointer method  -> {status}")
        print(f"Slicing method      -> {status}")
        print("-" * 50)

    # Additional performance verification for empty string edge case
    test_empty = is_palindrome_two_pointer("") and is_palindrome_slicing("")
    assert test_empty == True, "Empty string handling failed!"
    
    print("All tests passed successfully.")