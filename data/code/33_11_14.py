class StringCleaner:
    def clean(self, text):
        """
        Removes all spaces from the input string efficiently.
        
        Handles edge cases such as None or empty strings gracefully by returning 
        an empty result in those scenarios instead of raising exceptions.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A new string with all spaces removed, or an empty string if the input is invalid/empty.
        """
        # Handle non-string inputs and empty strings gracefully
        if not isinstance(text, str) or len(text.strip()) == 0:
            return ""

        # Use replace method for clarity; it's highly optimized in CPython (implemented in C)
        result = text.replace(" ", "")
        
        return result

if __name__ == '__main__':
    cleaner = StringCleaner()
    
    test_cases = [
        "Hello World",
        "",
        None,  # Should be handled gracefully as per requirements (though type check handles it)
        "   Multiple   Spaces   ",
        "NoSpacesHere123!",
        "\t\n\r\t\n\r"
    ]

    for test_input in test_cases:
        try:
            output = cleaner.clean(test_input if isinstance(test_input, str) else None)
            print(f"Input: {repr(test_input)} -> Output: '{output}'")
        except Exception as e:
            # Fallback just to be safe given the requirement says handle gracefully without error ideally
            print(f"Error processing input {test_input}: {e}")