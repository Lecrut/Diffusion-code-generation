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
            
            first_char = item[0] if len(item) > 0 else ''
            result.append(first_char)
        
        return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Hello", 
        "", 
        "World", 
        "!@#", 
        ""  # Testing empty string handling within the list
    ]

    extractor = FirstLetterExtractor()
    output = extractor.extract_all(samples)

    print("Input:", samples)
    print("Output:", output)