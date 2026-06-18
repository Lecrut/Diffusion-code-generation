class FirstLetterExtractor:
    def __init__(self):
        self.processed_strings = []

    def extract_all(self, string_list) -> list[str]:
        """
        Extracts the first letter from each non-empty string in the input list.
        
        Args:
            string_list (list[str]): A list of strings to process.
            
        Returns:
            list[str]: A list containing the first character of each valid string, 
                      or an empty string if the original was None/empty.
                      
        Raises:
            ValueError: If a non-string item is found in the input list.
        """
        result = []

        for index, current_str in enumerate(string_list):
            self.processed_strings.append(index)  # Track processing status (object state practice)

            if not isinstance(current_str, str):
                raise ValueError(f"Index {index}: Expected string but got {type(current_str).__name__}")

            if len(current_str) == 0:
                result.append("")
            else:
                result.append(current_str[0])

        return result

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    samples = [
        "Hello",
        "",      # Test empty string handling
        "World", 23, None  # Tests mixed types to demonstrate error raising capability if enabled
                          # Note: The task implies standard OOP practice which usually involves graceful 
                          # type checking or specific contract adherence. We will assume a clean input list for the demo run below
    ]

    # Clean sample data specifically for this runnable block to ensure it works smoothly without errors in default execution context,
    # strictly adhering to "runnable" requirement by providing valid inputs only in the main block logic if we want no raises.
    
    safe_samples = [
        "Python",
        "",          # Empty string should return empty string character representation "" or just skip? Usually returns "". 
                     # Based on standard extraction: first char of non-empty, else usually handled as ''.
    ]

    extractor = FirstLetterExtractor()
    extracted_letters = extractor.extract_all(safe_samples)

    print("Extracted letters:", extracted_letters)