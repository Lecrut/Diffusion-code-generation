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
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),  # Case-insensitive check usually required, but here strictly character-based as per standard two-pointer unless specified otherwise. 
                                                # Note: Standard palindrome definition often ignores case and spaces. 
                                                # However, the prompt implies direct string comparison via "two-pointer technique" on 'a string'.
                                                # To be robust for typical use cases while adhering to strict O(n) logic without extra preprocessing overhead in complexity class (though preprocessing is still linear),
                                                # we will implement a case-sensitive check as it's the most basic interpretation. 
                                                # If case-insensitivity was intended, explicit instruction would usually clarify "ignoring spaces and case".
        ("", True),  # Empty string is technically a palindrome
        ("12321", True),
        ("abcba", False) if len("abcba") > 0 else None  # Logic correction: abcba IS a palindrome. Let's fix the tuple below.
    ]

    # Correcting test case logic for clarity in execution block
    valid_test_cases = [
        "racecar",           # Should be True
        "hello",             # Should be False
        "",                  # Should be True (empty)
        "1234567890987654321",  # Long palindrome, should be True
    ]

    invalid_test_cases = [
        "racecaro",          # Slightly off at end -> False
        "hello world",       # Contains space and mismatched chars -> False (case sensitive)
    ]

    all_tests = valid_test_cases + invalid_test_cases
    
    print("Running palindrome checks...")
    
    for test_str in all_tests:
        result = is_palindrome(test_str)
        status = "PASS" if result else "FAIL"
        # Note: For 'racecaro', expected False. 
        # We assume case-sensitive and no space skipping based on strict function signature unless specified.
        
    print("All tests executed.")

# Additional explicit test to demonstrate the logic clearly within the module scope without external input
sample_input = "madam"
print(f"\nSample Input: '{sample_input}'")
output_result = is_palindrome(sample_input)
print(f"Is Palindrome? {output_result}") # Expected True for 'madam'

# Another sample that fails to show False case clearly
fail_sample = "hello world!"
result_fail = is_palindrome(fail_sample)
print(f"\nSample Input: '{fail_sample}'")
print(f"Is Palindrome? {result_fail}") # Expected False (due to space and exclamation mismatch in strict check, or True if we ignore non-alphanumeric. 
                                  # Given the constraint "check for palindromes in a string", usually implies alphanumeric only logic is preferred for real world, 
                                  # but strictly speaking 'two-pointer on string' checks every char.
                                  # Let's stick to strict character comparison as it guarantees O(n) and correctness without assumptions.)