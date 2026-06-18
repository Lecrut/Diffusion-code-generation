class FirstLetterExtractor:
    """A class to extract first letters from a list of strings."""

    def __init__(self):
        self._extracted_letters = []

    def extract_all(self, string_list):
        """
        Extracts the first letter from each non-empty string in the provided list.
        
        Args:
            string_list (list[str]): A list of strings to process.
            
        Returns:
            list[str]: A list containing the first character of each input string 
                      that is not empty or None, preserving order.
                      
        Raises:
            TypeError: If an element in the list is not a string.
        """
        result = []
        
        for item in string_list:
            if not isinstance(item, str):
                raise TypeError(f"Expected string type but got {type(item).__name__}")
            
            # Handle empty strings or None by skipping them based on problem constraints 
            # (implied "first letter" requires a character)
            if item and len(item.strip()) > 0:
                result.append(item[0])
        
        return result

if __name__ == '__main__':
    extractor = FirstLetterExtractor()

    sample_data = [
        "Hello",
        "",
        None, # Should be handled gracefully if type check allows or stripped; here we assume valid strings for simplicity in this specific task context unless strict typing is enforced. 
              # However, to strictly follow 'first letter', empty/None shouldn't yield a char.
              # Let's adjust logic: only take first char of non-empty string.
        "World",
        12345, # Invalid type per best practice check in method
    ]

    # Re-evaluating sample data for the specific constraint: 
    # The task says 'takes a list of strings'. If we pass an int, it's technically violating the input contract.
    # Let's use valid string samples to ensure robustness and avoid runtime errors on type checking if strict.
    
    clean_samples = [
        "Python",
        "",          # Empty string -> no first letter
        None,         # This might crash index access if not checked. 
                     # The method logic above checks 'if item'. If item is None, it's falsy in bool context but len() fails on None? No, len(None) raises TypeError immediately before the check.
                     # Correction: Must check isinstance first or handle non-string gracefully.
    ]

    # Final robust sample list strictly containing strings for demonstration of functionality
    final_samples = ["Hello", "", "World", "!"]  # '!' is a valid character
    
    try:
        output = extractor.extract_all(final_samples)
        print(f"Extracted letters from {final_samples}:")
        print(output)
        
        # Additional test case with mixed content (non-empty strings only expected to yield results in this logic if we skip empty/None implicitly by checking length > 0 after strip or just index access on non-falsy string)
        # To be safe and strictly 'first letter':
        sample_mixed = ["A", "B"]
        output2 = extractor.extract_all(sample_mixed)
        print(f"Extracted letters from {sample_mixed}:")
        print(output2)

    except Exception as e:
        print(f"An error occurred during extraction: {e}")