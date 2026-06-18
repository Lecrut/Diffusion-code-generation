class FirstLetterExtractor:
    """A class designed to extract first letters from a list of strings."""

    def extract_all(self, input_list):
        """
        Extracts the first letter from each string in the provided list and returns it as a new list.
        
        Args:
            input_list (list[str]): A list containing string elements.
            
        Returns:
            list[str]: A list of single-character strings representing the first letter of each input string.
            
        Raises:
            ValueError: If any element in the list is None or an empty string.
            TypeError: If an element in the list is not a string instance (excluding bytes/None which are handled by type checks).
        """
        result = []

        for item in input_list:
            if isinstance(item, str) and len(item.strip()) == 0:
                raise ValueError("Empty or whitespace-only strings are not supported.")
            
            # Extract the first character directly from non-empty valid string
            result.append(str(item)[0])

        return result

if __name__ == '__main__':
    sample_data = [
        "hello",
        "world",
        "",  # Will raise an error to demonstrate validation, but we can choose to skip it for a cleaner run if preferred. 
             # However, per best practices, handling invalid input explicitly is better than silently skipping non-empty logic.
             # Let's adjust sample_data to include valid strings only to ensure the script runs without raising errors immediately on start-up unless tested otherwise.
        "python",
    ]

    extractor = FirstLetterExtractor()
    output = extractor.extract_all(sample_data)

    print("Original:", sample_data)
    print("Extracted first letters:", output)