class StringUtils:
    def is_palindrome(self, s: str) -> bool:
        """
        Checks if a string is a palindrome using an in-place comparison technique 
        by converting to list and modifying elements directly (two-pointer approach).
        
        Args:
            s (str): Input string
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        # Convert string to list for mutability as per in-place requirement
        char_list = list(s)
        left, right = 0, len(char_list) - 1
        
        while left < right:
            # Compare characters from both ends moving inward
            if char_list[left] != char_list[right]:
                return False
            
            # Move pointers towards center
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("No 'x' in Nixon", True),
        ("12321", True),
        ("python", False)
    ]

    test_string = "racecar"  # Default sample value
    
    print(f"Testing palindrome: '{test_string}'")
    
    if StringUtils.is_palindrome(test_string):
        result_msg = "is a palindrome"
    else:
        result_msg = "is not a palindrome"
        
    print(f"The string {result_msg}")

    # Verify with multiple test cases using list comprehension for output formatting
    results = [f"'{s}' is {'a' if StringUtils.is_palindrome(s) else 'not'} a palindrome" 
               for s, expected in test_cases]
    
    print("\nTest Results:")
    for result in results:
        print(result)