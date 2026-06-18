def is_palindrome_optimized(s: str) -> bool:
    """
    Check if a string is a palindrome by comparing it with its reverse.
    
    This implementation creates a reversed copy of the input string and compares 
    it directly to the original. While creating a full reversed copy uses O(n) memory,
    this approach is highly optimized for readability and performance in Python due to 
    efficient C-level string slicing operations. For extremely large inputs where 
    minimizing peak memory usage below O(n) is critical, an iterative two-pointer 
    comparison could be used instead (though that would require explicit loop logic).
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "radar",           # Should be True
        "madam",           # Should be True
        "hello",           # Should be False
        "",                # Edge case: empty string, should be True
        "a",               # Single character, should be True
        "abba",            # Should be True
        "abcde",           # Should be False
    ]

    for test_string in test_cases:
        result = is_palindrome_optimized(test_string)
        print(f"String: '{test_string}' -> Is Palindrome: {result}")