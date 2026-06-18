class FirstLetterExtractor:
    """A class that extracts first letters from a list of strings."""

    def extract_all(self, string_list):
        """
        Extracts the first letter from each non-empty string in the provided list.

        Args:
            string_list (list[str]): A list of input strings.

        Returns:
            list[str]: A list containing the first character of each non-empty string.
                       Empty strings or None values are skipped to avoid errors, 
                       but if strict behavior is needed for empty strings returning empty char,
                       this implementation returns nothing for them per common best practices 
                       unless specified otherwise. Here we assume meaningful input: 
                       If a string exists and has length > 0, return its first character;
                       else skip it to prevent runtime errors on invalid inputs (e.g., None).

        Raises:
            TypeError: If an element in the list is not a string instance or contains non-string types.
        """
        result = []
        
        # Validate input type and iterate safely
        for item in string_list:
            if isinstance(item, str) and len(item) > 0:
                result.append(item[0])
            elif not isinstance(item, (str)): 
                raise TypeError(f"Expected a string or skip invalid types; encountered {type(item).__name__}")

        return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements: no user input or external dependencies.
    samples = [
        "Hello",
        "Python",
        "",          # Empty string - will be skipped based on logic above for robustness, 
                     # but if strict first-char extraction is needed including edge cases like returning empty char, adjust accordingly.
                    # Here we assume meaningful data: skipping empty strings avoids index error.
    ]

    extractor = FirstLetterExtractor()
    
    try:
        extracted_letters = extractor.extract_all(samples)
        print("Extracted letters:", [str(l).lower() for l in extracted_letters])
        
    except TypeError as e:
        print(f"Error occurred during extraction: {e}")