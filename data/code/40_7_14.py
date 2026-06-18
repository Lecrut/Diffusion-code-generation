class StringProcessor:
    """A utility class for basic string processing operations."""

    def get_first_letter_of_first_word(self, text: str) -> str | None:
        """
        Returns the first letter of the very first word in the input string.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str or None: The first character if a non-empty word exists, 
                        otherwise returns None. Handles leading whitespace and empty strings gracefully.
                        
        Example:
            >>> processor = StringProcessor()
            >>> processor.get_first_letter_of_first_word("  Hello World")
            'H'
            >>> processor.get_first_letter_of_first_word("")
            None
        """
        if not text or not isinstance(text, str):
            return None
        
        # Strip leading whitespace to find the start of the first word
        stripped_text = text.lstrip()
        
        # If string is empty after stripping, no words exist
        if not stripped_text:
            return None
            
        # Get the first character directly from the original string at the index 
        # where the non-whitespace content begins. This avoids creating a new substring object unnecessarily.
        start_index = 0
        
        while start_index < len(text) and text[start_index] == ' ':
            start_index += 1
            
        if start_index >= len(text):
            return None
            
        char_at_start = text[start_index]
        
        # Check if the character is alphabetic to ensure it's a letter (optional strictness based on "letter" definition)
        # If purely ASCII letters are required:
        import string
        
        if not char_at_start.isalpha():
            return None
            
        return char_at_start

if __name__ == '__main__':
    processor = StringProcessor()
    
    test_cases = [
        "  Hello World",
        "\t\n\tPython Programming",
        "",
        "   ",
        "123abc456def",
        "!@#$%Hello"
    ]
    
    for text in test_cases:
        result = processor.get_first_letter_of_first_word(text)
        print(f'Input: {repr(text)} -> Output: {result}')