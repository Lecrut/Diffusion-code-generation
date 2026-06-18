class TextProcessor:
    """A utility class for text processing operations."""

    def clean_text(self, text):
        """
        Removes all whitespace characters from the input string.

        Args:
            text (str): The input string containing potential whitespace.

        Returns:
            str: A new string with all leading, trailing, and internal 
                 whitespace characters removed.
        
        Raises:
            TypeError: If the input is not a string instance.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected 'str', got '{type(text).__name__}'")

        return ''.join(char for char in text if not char.isspace())

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    processor = TextProcessor()

    test_cases = [
        "  Hello World! ",           # Leading/trailing spaces and internal space
        "\t\n\r\t\n",                # Various whitespace characters only
        "NoSpacesHere123!",          # No whitespace to remove
        "",                          # Empty string
        "   \t\n  Mixed    text  \r" # Complex mix of whitespaces
    ]

    print("Testing clean_text method:")
    for i, test_input in enumerate(test_cases, 1):
        try:
            result = processor.clean_text(test_input)
            status = "Success" if len(result) == len(test_input.rstrip()) else f"Output length differs from stripped input (expected {len(''.join(c for c in test_input if not c.isspace()))}) -> got {len(result)})" 
            # Note: The check above is slightly redundant logic-wise but demonstrates the result clearly
            print(f"Test Case {i}: Input='{test_input}'")
        except Exception as e:
            status = f"Error: {e}"
        
    # Demonstrate a specific case with expected output length calculation for clarity in logs
    sample_text = "   Hello World!  \t\n\r"
    clean_result = processor.clean_text(sample_text)
    
    print("\nDetailed Example:")
    print(f"Original text: '{sample_text}'")
    print(f"Cleaned result: '{clean_result}' (Length: {len(clean_result)})")