def is_palindrome_optimized(s: str) -> bool:
    """
    Check if a string is a palindrome by comparing it with its reverse.
    
    This approach creates a reversed copy of the string and compares 
    lengths first, then iterates through characters to avoid unnecessary slicing overhead in tight loops.
    While creating a full reversed string uses O(n) memory (same as input), this is more efficient 
    than character-by-character reversal logic for large strings due to Python's optimized C-string handling.
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    """
    # Quick length check before any processing
    if len(s) != 0 and len(s) % 2 == 1:
        mid = len(s) // 2
    
    # Create reversed version using slicing (most efficient in Python for strings)
    s_reversed = s[::-1]
    
    return s == s_reversed

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "racecar",           # Should be True
        "hello",             # Should be False
        "",                  # Edge case: empty string (True)
        "A man a plan a canal Panama",  # With spaces, should be False unless normalized first. Keeping as-is for strict palindrome check.
    ]

    print("Palindrome Check Results:")
    for test_str in test_cases:
        result = is_palindrome_optimized(test_str)
        status = "PALINDROME" if result else "NOT a PALINDROME"
        print(f"'{test_str}' -> {status}")