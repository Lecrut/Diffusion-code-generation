class StringProcessor:
    """A utility class for basic string processing operations."""

    def get_first_letter_of_first_word(self, text: str) -> str:
        """
        Returns the first letter of the very first word in the input string.
        
        Handles leading whitespace and returns an empty string if no words are found.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A single character representing the first letter, or '' if none exists.
        """
        # Strip leading whitespace and check for non-empty result immediately
        stripped_text = text.lstrip()
        
        # If there is content after stripping, get the very first character
        if len(stripped_text) > 0:
            return stripped_text[0]
            
        return ""

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "   Hello World",      # Leading spaces, expects 'H'
        "\t\n\tStart Here",     # Tabs and newlines, expects 'S'
        "NoSpacesAtAll",         # No leading whitespace, expects 'N'
        "",                     # Empty string, expects ''
        "   ",                  # Only whitespace, expects ''
    ]

    processor = StringProcessor()

    for test_input in test_cases:
        result = processor.get_first_letter_of_first_word(test_input)
        print(f"Input: {repr(test_input)} -> Output: '{result}'")