import string

class StringUtils:
    """A utility class providing optimized string manipulation methods."""

    def is_palindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome using an in-place comparison technique.
        
        This method ignores case and non-alphanumeric characters by converting the 
        input to lowercase and filtering out unwanted characters before comparing.
        The algorithm uses two pointers starting from both ends of the filtered string,
        moving inward while comparing corresponding characters for equality.
        
        Args:
            s (str): The input string to check
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        # Filter and normalize the string in one pass using list comprehension
        filtered_chars = [c.lower() for c in s if c.isalnum()]
        
        left = 0
        right = len(filtered_chars) - 1
        
        while left < right:
            char_left = filtered_chars[left]
            char_right = filtered_chars[right]
            
            # If characters don't match, it's not a palindrome
            if char_left != char_right:
                return False
            
            left += 1
            right -= 1
        
        return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("12321", True),
        ("12345", False),
        ("", True),  # Empty string is technically a palindrome
        ("a", True),  # Single character is always a palindrome
    ]

    print("Running StringUtils.is_palindrome tests...\n")

    for test_input, expected in test_cases:
        result = StringUtils().is_palindrome(test_input)
        
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{test_input}' -> Expected: {expected}, Got: {result}")

    # Additional demonstration with a custom string
    demo_string = "Madam"
    is_palindrome_demo = StringUtils().is_palindrome(demo_string)
    
    print("\n--- Demo ---")
    print(f"Testing '{demo_string}': {'Is Palindrome' if is_palindrome_demo else 'Not a Palindrome'}")