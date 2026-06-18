class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Check if a given string is a palindrome.

        This method considers only alphanumeric characters and ignores case sensitivity.
        It handles Unicode strings correctly by normalizing them before comparison.

        Args:
            text (str): The input string to check for palindromic property.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Normalize the string to lowercase and keep only alphanumeric characters
        normalized_text = ''.join(char.lower() for char in text if char.isalnum())
        
        return normalized_text == normalized_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the is_palindrome method without user input
    
    # Test cases: (input_string, expected_output)
    test_cases = [
        ("A man a plan a canal Panama", True),
        ("race car", True),
        ("Hello World!", False),
        ("Was it a car or a cat I saw?", True),
        ("12321", True),
        ("12345", False),
        ("", True),  # Empty string is technically a palindrome
        ("a", True),   # Single character is a palindrome
    ]

    operations = StringOperations()

    print("Running Palindrome Tests...\n")

    for i, (input_str, expected) in enumerate(test_cases):
        result = operations.is_palindrome(input_str)
        
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i+1}: '{input_str}' -> Expected: {expected}, Got: {result} [{status}]")

    # Additional demonstration with a custom string
    demo_string = "Madam, I'm Adam."
    is_demo_palindrome = operations.is_palindrome(demo_string)
    
    print(f"\nDemo Test:")
    print(f"Input: '{demo_string}'")
    print(f"Is Palindrome? {is_demo_palindrome}")