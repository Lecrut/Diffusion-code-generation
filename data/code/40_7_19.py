class StringProcessor:
    """A utility class for basic string processing operations."""

    def get_first_letter_of_first_word(self, text: str) -> str | None:
        """
        Returns the first letter of the very first word in the input string.
        
        This method is efficient and readable by skipping non-alphabetic characters
        until an alphabetic character is found, then returning it immediately.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str | None: The first letter of the first word if found, otherwise None.
                        If no letters are present in the entire string, returns None.
                        
        Examples:
            >>> sp = StringProcessor()
            >>> sp.get_first_letter_of_first_word("  Hello World")
            'H'
            >>> sp.get_first_letter_of_first_word("!@#$%")
            None
            >>> sp.get_first_letter_of_first_word("")
            None
        """
        if not text:
            return None

        for char in text:
            if char.isalpha():
                return char
        
        return None

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "  Hello World",
        "!@#$%",
        "",
        "...start here...",
        "12345abcde"
    ]

    processor = StringProcessor()

    print("String Processor Test Results")
    print("-" * 30)

    for test_input in test_cases:
        result = processor.get_first_letter_of_first_word(test_input)
        display_text = f'Input: "{test_input}" -> Output: {result}'
        print(display_text)