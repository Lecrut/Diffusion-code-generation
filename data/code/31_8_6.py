class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Check if a given string is a palindrome ignoring spaces and case sensitivity.

        Args:
            text (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        
        Examples:
            >>> ops = StringOperations()
            >>> ops.is_palindrome("A man a plan a canal Panama")
            True
            >>> ops.is_palindrome("Hello World")
            False
        """
        # Normalize the string by removing spaces and converting to lowercase
        normalized_text = text.replace(' ', '').lower()
        
        # Check if the normalized string is equal to its reverse
        return normalized_text == normalized_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        "A man a plan a canal Panama",  # Should be True
        "race car",                     # Should be True
        "Hello World",                  # Should be False
        "",                            # Edge case: Empty string should be True
        "12321",                       # Numeric palindrome in string form, should be True
    ]

    operations = StringOperations()

    print("Palindrome Check Results:")
    for test_input in test_cases:
        result = operations.is_palindrome(test_input)
        status = "True" if result else "False"
        print(f'Input: "{test_input}" -> {status}')