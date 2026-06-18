def is_palindrome(s: str) -> bool:
    """
    Determines if a given string is a palindrome, ignoring case 
    and non-alphanumeric characters. Handles edge cases like empty strings
    or strings containing only symbols.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: convert to lowercase and keep only alphanumeric characters
    normalized = ''.join(c.lower() for c in s if c.isalnum())
    
    # An empty string or one with no valid characters after filtering 
    # is technically considered a palindrome as it reads the same forwards and backwards.
    return normalized == normalized[::-1]

if __name__ == '__main__':
    # Sample test cases covering various edge cases and normal inputs
    test_cases = [
        "",                           # Empty string - should be True
        "a",                          # Single character - should be True
        "A man a plan a canal Panama!",  # Classic palindrome with symbols/case - should be True
        "hello world",                # Normal non-palindrome - should be False
        "!@#$%",                      # Only symbols - should be True (empty after filter)
        "12321",                      # Numeric palindrome - should be True
        "No 'x' in Nixon!",           # Mixed case and punctuation - should be True
    ]

    for test_string in test_cases:
        result = is_palindrome(test_string)
        print(f"'{test_string}' -> {result}")