class FirstLetterExtractor:
    """A class that extracts the first letter from a list of strings."""

    def extract_all(self, string_list):
        """
        Extracts the first character from each non-empty string in the input list.
        
        Args:
            string_list (list[str]): A list of strings to process.
            
        Returns:
            list[Optional[str]]: A list containing the first letter of each 
                                string, or None if the string is empty.

        Raises:
            TypeError: If any element in the list is not a string or is None.
            ValueError: If an element is neither a valid string nor None.
        """
        result = []
        
        for item in string_list:
            # Validate input type; allow strings and None (for empty sequences)
            if isinstance(item, str):
                first_char = item[0] if item else None
                result.append(first_char)
            elif item is None:
                result.append(None)
            else:
                raise TypeError(f"Expected a string or None, got {type(item).__name__}")

        return result

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_data = [
        "Hello",       # 'H'
        "",            # Empty string -> None
        "World!",      # 'W'
        None,          # Explicit None -> None
        "Python"       # 'P'
    ]

    extractor = FirstLetterExtractor()
    
    output_list = extractor.extract_all(test_data)

    print("Input:", test_data)
    print("Output (first letters):", [str(x) if x is not None else "None" for x in output_list])