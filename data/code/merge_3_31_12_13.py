def is_palindrome_two_pointer(s: str) -> bool:
    """
    Determines if a string is a palindrome using the two-pointer approach.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters and case-insensitive comparison logic handled by converting to lower later or checking directly
        # However, standard definition usually implies ignoring spaces/punctuation unless specified. 
        # Given the task asks for "optimized method" on a string without specifying rules, we assume strict character match first.
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

def is_palindrome_slicing(s: str) -> bool:
    """
    Determines if a string is a palindrome using string slicing and comparison.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Reverse the entire string and compare with original
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        "racecar",           # True (standard palindrome)
        "A man a plan a canal Panama",  # False if strict, but usually considered true with filtering. 
                             # Since we are not implementing the filter logic explicitly in these functions to keep them simple and efficient as per general string operations unless specified:
                             # Let's test strictly first then maybe add a helper for robustness? 
                             # The prompt asks for "optimized method". Strict equality is O(N) time, slicing creates copy. Two pointer avoids copy.
        "hello",             # False
        "",                  # True (empty string)
        "madam",             # True
    ]

    print("Testing Palindrome Detection\n")
    
    for test_str in test_cases:
        result_ptr = is_palindrome_two_pointer(test_str)
        result_slice = is_palindrome_slicing(test_str)
        
        status = "PASS" if result_ptr == result_slice else "MISMATCH (Note on strictness)"
        print(f'String: "{test_str}"')
        print(f'  Two-Pointer Result: {result_ptr}')
        print(f'  Slicing Result:     {result_slice}')
        print(f'  Status:             {status}\n')

    # Example with a case-insensitive, space/punctuation-aware palindrome for demonstration of utility
    robust_test = "A man, a plan, a canal: Panama"
    
    def is_palindrome_robust(s):
        """Helper to handle real-world palindromes (ignores non-alphanumeric and case)."""
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return is_palindrome_slicing(cleaned)

    robust_result = is_palindrome_robust(robust_test)
    print(f"Robust Test: '{robust_test}'")
    print(f'  Is Palindrome (ignoring case/punctuation): {robust_result}')