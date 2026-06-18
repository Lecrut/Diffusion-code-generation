class StringUtils:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Checks if a given string is a palindrome using two pointers (in-place logic).
        
        This approach compares characters from the start and end of the string moving
        towards the center. Non-alphanumeric characters are ignored during comparison,
        but they do not shift positions to maintain true in-place efficiency regarding data movement.

        Args:
            s (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome (ignoring non-alphanumeric chars), False otherwise.
        """
        # Convert to lowercase for case-insensitive comparison
        s_lower = s.lower()
        
        left, right = 0, len(s) - 1
        
        while left < right:
            current_left_char = None
            current_right_char = None
            
            # Move inward from both sides until alphanumeric characters are found at each pointer position that matches the target side index (conceptually skipping non-alphanumeric without moving indices themselves to avoid shifting operations which could be O(N))
            while left < right and not s_lower[left].isalnum():
                current_left_char = None
            
            if current_left_char is None:
                # Skip characters from left until we find a valid one or cross the pointer
                pass 
                
            # Actually, let's refine to just skip without shifting data.
            while left < right and not s_lower[left].isalnum():
                left += 1
            
            if left >= right: break

            # Move inward from both sides until alphanumeric characters are found at each pointer position that matches the target side index (conceptually skipping non-alphanumeric without moving indices themselves to avoid shifting operations which could be O(N))
            
        # Corrected logic implementation below for clarity and correctness
            
        s_lower = s.lower()
        l, r = 0, len(s) - 1

        while l < r:
            if not s_lower[l].isalnum():
                l += 1
                continue
            if not s_lower[r].isalnum():
                r -= 1
                continue
            
            if s_lower[l] != s_lower[r]:
                return False
                
            l += 1
            r -= 1
            
        return True

if __name__ == '__main__':
    # Hard-coded sample values to test the functionality without user input or files.
    
    tests = [
        ("A man a plan a canal Panama", True),   # Classic palindrome with spaces/punctuation
        ("racecar", True),                        # Simple palindrome
        ("hello world", False),                   # Not a palindrome
        ("Was it a car or a cat I saw?", True),  # Ignoring case and non-alphanumerics
        (1234, "Not applicable"),                 # Placeholder for potential int input if needed later, though type hint says str. We assume string only per task spec context but test with strings strictly.
        ("", True),                               # Empty string is palindrome
        ("a", True),                              # Single char is palindrome
    ]

    for i in range(0, len(tests)):
        if isinstance(tests[i], tuple):
            s = tests[i][0]
            expected = tests[i][1]
            result = StringUtils.is_palindrome(s)
            print(f"Test {i}: Input='{s}' -> Expected: {expected}, Result: {result} | {'PASS' if result == expected else 'FAIL'}")
        elif isinstance(tests[i], int):
             # Skip non-string test case as per logic focus on string input unless specified otherwise. 
             # If the user intended to pass integers, they would fail type checking in a strict implementation here assuming str only based on "checks if a given **string**".
             print(f"Test {i}: Skipping integer input '{tests[i]}'")

    # Final explicit test run for demonstration without loop overhead verbosity if desired, but the loop above is sufficient.