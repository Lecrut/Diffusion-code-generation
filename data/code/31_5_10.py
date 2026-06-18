def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if 's' is a palindrome, False otherwise.

    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1).
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or file access
    test_cases = [
        "racecar",       # Should be True
        "hello",         # Should be False
        "",              # Edge case: empty string, should be True
        "a",             # Single character, should be True
        "Madam",         # Case-sensitive check (False by default unless specified), 
                        # note: standard palindrome check is usually case-insensitive.
                        # However, the task specifies checking on a 'string'.
                        # We will implement strict equality here based on s[left] != s[right].
                        # If case insensitivity was intended without explicit prompt, it's an assumption.
                        # To be safe and strictly follow "check for palindromes in a string", 
                        # we assume the input is the exact character sequence to match itself forwards/backsordsly.
        "abba",          # Should be True
    ]

    print("Running palindrome checks...")
    for test_str in test_cases:
        result = is_palindrome(test_str)
        status = "True" if result else "False"
        formatted_result = f"'{test_str}' -> {status}"
        print(formatted_result)