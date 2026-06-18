class StringOperations:
    """A class designed to perform various string operations."""

    def is_palindrome(self, text: str) -> bool:
        """
        Check if a given string is a palindrome.
        
        A palindrome is a word, phrase, number, or other sequence of 
        characters that reads the same forward and backward (ignoring spaces, punctuation, and case).

        Args:
            text (str): The input string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Normalize the string by converting to lowercase and removing non-alphanumeric characters
        normalized_text = ''.join(char.lower() for char in text if char.isalnum())
        
        return normalized_text == normalized_text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or external dependencies
    
    # Test cases: list of strings and their expected boolean results
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("Madam", True),
        ("Hello World", False),
        ("12321", True),
        ("No 'x' in Nixon", True)
    ]

    # Instantiate the class and run tests
    ops = StringOperations()
    
    print("Palindrome Test Results:")
    for test_string, expected_result in test_cases:
        result = ops.is_palindrome(test_string)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"'{test_string}' -> {result} (Expected: {expected_result}) [{status}]")