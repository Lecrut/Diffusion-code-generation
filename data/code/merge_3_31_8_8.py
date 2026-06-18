class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Checks if a given string is a palindrome.

        A palindrome is a word, phrase, number, or other sequence of characters 
        that reads the same forward and backward (ignoring spaces, punctuation, 
        and case differences). This implementation normalizes the input by removing 
        non-alphanumeric characters and converting to lowercase before comparison.

        Args:
            text (str): The string to check for palindrome property.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Normalize the string: keep only alphanumeric characters and convert to lower case
        normalized_text = ''.join(char.lower() for char in text if char.isalnum())
        
        # Check if the normalized string equals its reverse
        return normalized_text == normalized_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or external dependencies
    
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a cat and I?", True),
        ("Madam", True),
        ("hello", False),
        ("" , True),  # Empty string is technically a palindrome
    ]

    operations = StringOperations()

    print("Testing StringOperations.is_palindrome method:\n")
    
    for test_input, expected_result in test_cases:
        result = operations.is_palindrome(test_input)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"Input: '{test_input}' | Expected: {expected_result} | Result: {result} [{status}]")

    # Additional demonstration of usage with a custom string
    demo_string = "1234567890"
    is_pal_demo = operations.is_palindrome(demo_string)
    print(f"\nDemo Input: '{demo_string}' | Is Palindrome? {is_pal_demo}")