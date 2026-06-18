class StringCaseManipulator:
    """A class to handle various case manipulation operations on strings."""

    def transform(self, text):
        """
        Transforms a given string based on specific case requirements.
        
        This method acts as the main entry point for case transformation.
        It currently returns the input text unchanged but is designed 
        to be extended with logic that delegates to specialized methods.
        
        Args:
            text (str): The input string to manipulate.
            
        Returns:
            str: The transformed string. Currently identical to input,
                 ready for specific transformation calls via other methods.
        """
        return text

    def lowercase(self, text):
        """Converts the entire string to lowercase."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.lower()

    def uppercase(self, text):
        """Converts the entire string to uppercase."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.upper()

    def title_case(self, text):
        """Capitalizes each word in the string (Title Case)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        # Split into words, capitalize each, then join back together.
        return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    manipulator = StringCaseManipulator()

    test_strings = [
        "hello world",
        "PYTHON IS FUN",
        "this is a random sentence"
    ]

    print("Original Strings:")
    for s in test_strings:
        print(f"'{s}'")

    print("\nTransformed Results:\n")

    # Demonstrate lowercase transformation
    print("--- Lowercase ---")
    for original in test_strings:
        result = manipulator.lowercase(original)
        print(f"Input: '{original}' -> Output: '{result}'")

    # Demonstrate uppercase transformation
    print("\n--- Uppercase ---")
    for original in test_strings:
        result = manipulator.uppercase(original)
        print(f"Input: '{original}' -> Output: '{result}'")

    # Demonstrate title case transformation
    print("\n--- Title Case ---")
    for original in test_strings:
        result = manipulator.title_case(original)
        print(f"Input: '{original}' -> Output: '{result}'")