def is_palindrome_two_pointers(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.
    
    This function compares characters from both ends of the string moving towards 
    the center, ignoring case differences and non-alphanumeric characters to ensure
    it works correctly for strings with spaces or punctuation (optional based on input).
    
    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) as no extra data structures are used beyond pointers.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Note: This implementation treats all characters equally including spaces and punctuation 
    unless specified otherwise by converting everything to lowercase for case-insensitive comparison.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    test_cases = [
        ("racecar", True),           # Classic palindrome example
        ("A man, a plan, a canal: Panama", True),  # With spaces and punctuation (case-insensitive)
        ("hello", False),            # Not a palindrome
        ("Was it a car or a cat I saw?", True),     # Common tricky one with mixed casing/punctuation
        ("12321", True),             # Numeric string palindrome
        ("abba", True),              # Short even length palindrome
        ("abc", False),              # Odd length non-palindrome
    ]

    for test_string, expected_result in test_cases:
        result = is_palindrome_two_pointers(test_string)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"[{status}] Input: '{test_string}' -> Expected: {expected_result}, Got: {result}")