def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome using the two-pointer technique.
    
    The function compares characters from both ends of the string moving towards 
    the center, ignoring case and non-alphanumeric characters to ensure accurate 
    evaluation based on alphanumeric content only (optional behavior; here we compare raw chars).
    
    Time Complexity: O(n) - Each character is visited at most once.
    Space Complexity: O(1) - Only two pointers are used for traversal without extra storage proportional to input size.

    Args:
        s (str): The string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Compare characters at both pointers
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    
    # Test Case 1: Simple palindrome
    assert is_palindrome("radar") == True, "Test case 1 failed"
    
    # Test Case 2: Non-palindrome with different length
    assert is_palindrome("hello") == False, "Test case 2 failed"
    
    # Test Case 3: Palindrome with spaces (checking raw string as per two-pointer logic on full string)
    # Note: If the requirement was to ignore non-alphanumeric characters, this would need adjustment. 
    # Based on strict O(n) implementation of 'check for palindromes in a string' without explicit instructions 
    # to filter, we assume direct comparison unless specified otherwise. However, typically palindrome checks
    # imply alphanumeric focus. Let's adjust logic slightly within the function above implicitly by just comparing chars directly.
    # Actually, let's stick strictly to what was implemented: raw character comparison for maximum fidelity to "two-pointer on string".
    
    assert is_palindrome("A man a plan a canal Panama") == False  # Raw check fails due to case and spaces mismatched positions if not filtered? 
                          # Wait, 'A' vs 'a', space vs n... This raw version returns False correctly.
                          
    # Let's provide a test that works for typical user expectation (case-insensitive alphanumeric) by modifying logic slightly inside the function below
    # to be robust: re-implementing with case-insensitivity and filtering non-alphabetic characters for better utility, 
    # while keeping O(n).

def is_palindrome_v2(s: str) -> bool:
    """
    Enhanced version that checks palindrome ignoring case and non-alphanumeric characters.
    
    Time Complexity: O(n) - Single pass through the string.
    Space Complexity: O(1) - Two pointers only, no extra data structures.
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
    # Re-run tests with the enhanced version for better usability as "check palindrome" usually implies semantic check.
    
    assert is_palindrome_v2("radar") == True, "Test case 1 failed (enhanced)"
    assert is_palindrome_v2("hello") == False, "Test case 2 failed (enhanced)"
    assert is_palindrome_v2("A man a plan a canal Panama") == True, "Test case 3 failed"
    assert is_palindrome_v2("No 'x' in Nixon") == True, "Test case 4 failed"
    
    print("All tests passed successfully.")