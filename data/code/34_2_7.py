class StringCapitalizer:
    """A class to capitalize specific parts of a string."""

    def capitalize_words(self, input_string):
        """
        Capitalizes only the first letter of each word in the given string.

        Args:
            input_string (str): The string to process.

        Returns:
            str: A new string with the first letter of each word capitalized.
        
        Example:
            >>> capitalizer = StringCapitalizer()
            >>> result = capitalizer.capitalize_words("hello world")
            >>> print(result)
            'Hello World'
        """
        if not isinstance(input_string, str):
            raise TypeError(f"Expected string input, got {type(input_string).__name__}")

        # Split the string into words based on whitespace
        words = input_string.split()
        
        # Capitalize the first letter of each word and join them back with spaces
        capitalized_words = [word.capitalize() for word in words]
        
        return ' '.join(capitalized_words)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    
    # Test case 1: Normal sentence
    test_input_1 = "hello world this is a test"
    
    # Test case 2: Sentence with mixed casing and punctuation attached (basic handling)
    test_input_2 = "python programming language is fun!"
    
    # Test case 3: Single word
    test_input_3 = "code"
    
    capitalizer = StringCapitalizer()
    
    print("Test Case 1:")
    result_1 = capitalizer.capitalize_words(test_input_1)
    print(f"Input: '{test_input_1}'")
    print(f"Output: '{result_1}'\n")
    
    print("Test Case 2:")
    result_2 = capitalizer.capitalize_words(test_input_2)
    print(f"Input: '{test_input_2}'")
    print(f"Output: '{result_2}'\n")
    
    print("Test Case 3:")
    result_3 = capitalizer.capitalize_words(test_input_3)
    print(f"Input: '{test_input_3}'")
    print(f"Output: '{result_3}'")