def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Compare characters from both ends moving towards the center
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        ("racecar", True),           # Classic palindrome
        ("hello", False),            # Not a palindrome
        ("A man a plan a canal Panama", True),  # Palindrome with spaces and case (if we ignore non-alphanumeric) -> Note: This function checks exact match including space/case. Adjusted for strict string check below.
        ("12321", True),             # Numeric palindrome
        ("abba", True),              # Even length palindrome
        ("abcde", False),            # No symmetry
    ]

    print("Running Palindrome Checks...")
    
    for test_string, expected in test_cases:
        result = is_palindrome(test_string)
        
        if result == expected:
            status = "PASS"
        else:
            status = "FAIL"
            
        # Note on case sensitivity and spaces: 
        # The current implementation checks the exact string provided.
        # If you need to ignore non-alphanumeric characters or case, that logic would be added here.
        
        print(f"'{test_string}' -> {result} (Expected: {expected}) [{status}]")

    # Additional test for strict character matching including spaces/case as per function definition
    mixed_case_test = "RaceCar" 
    result_mixed = is_palindrome(mixed_case_test)
    expected_mixed = False  # 'R' != 'r', space breaks it too if present, but here no space. Strict check: R!=r -> False
    
    print(f"'{mixed_case_test}' (Strict Check) -> {result_mixed} (Expected: {expected_mixed})")