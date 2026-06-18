class StringProcessor:
    """A class to process strings with optimized operations."""
    
    def remove_spaces(self, input_str: str) -> str:
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            input_str (str): The input string containing potential spaces.
            
        Returns:
            str: A new string with all spaces removed.
        """
        return ''.join(char for char in input_str if not (' ' == char))

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    test_cases = [
        "Hello World",
        "  Multiple   Spaces  ",
        "NoSpacesHere",
        " Python Programming Language",
        ""
    ]

    processor = StringProcessor()

    for i, original in enumerate(test_cases):
        result = processor.remove_spaces(original)
        print(f"Input {i+1}: '{original}'")
        print(f"Output:   '{result}'\n")