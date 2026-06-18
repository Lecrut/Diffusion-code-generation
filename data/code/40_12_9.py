class FirstLetterExtractor:
    """A class that extracts first letters from a list of strings."""

    def extract_all(self, string_list):
        """
        Extracts the first letter from each non-empty string in the input list.

        Args:
            string_list (list[str]): A list of strings to process.

        Returns:
            list[str]: A list containing the first character of each non-empty 
                      string, or an empty string if the original was empty.
        
        Raises:
            TypeError: If any element in the list is not a string.
        """
        result = []
        for item in string_list:
            if not isinstance(item, str):
                raise TypeError(f"Expected string, got {type(item).__name__}")
            
            first_char = ''
            if len(item) > 0:
                first_char = item[0]
            result.append(first_char)
        
        return result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_data = [
        "Hello",
        "",
        "World",
        "!@#",
        123,  # This will trigger a TypeError as per best practices to validate types
    ]

    extractor = FirstLetterExtractor()
    
    try:
        output = extractor.extract_all(test_data)
        print("Extracted first letters:", output)
        
        # Demonstrate error handling with the invalid type in sample data
        if len(output) > 0 and isinstance(output[-1], str):
            pass 
    except TypeError as e:
        print(f"Error occurred during extraction: {e}")