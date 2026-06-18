class StringCaseManipulator:
    """A utility class to handle case manipulation of strings."""

    def transform(self, text):
        """
        Transforms a string based on specific casing requirements.
        
        This method is intended as an entry point but currently delegates 
        the actual transformation logic to its specialized methods for clarity.
        In this implementation, it defaults to returning lowercase unless 
        overridden by calling specific helper methods directly or via subclassing.

        Args:
            text (str): The input string to be transformed.

        Returns:
            str: A new string with the applied case transformation.
            
        Note: Since no explicit mode is passed, this method defaults to lowercase 
        for consistency in a single-module structure without external configuration.
        """
        return self.lower(text) if text else ""

    def lower(self, text):
        """Converts all characters in the string to lowercase."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.lower()

    def upper(self, text):
        """Converts all characters in the string to uppercase."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.upper()

    def title(self, text):
        """Capitalizes each word in the string (Title Case)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        # Python's built-in title() handles non-cased characters correctly 
        # by leaving them unchanged while capitalizing the first letter of words.
        return text.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()

    sample_text = "hello world! this is a test string."
    
    print("Original:", repr(sample_text))
    print("Lowercase:", repr(manipulator.transform(sample_text))) # Defaults to lower
    
    # Demonstrate individual methods as requested by the task structure
    result_lower = manipulator.lower(sample_text)
    result_upper = manipulator.upper(sample_text)
    result_title = manipulator.title(sample_text)

    print("\nSpecific Transformations:")
    print("Lowercase:", repr(result_lower))
    print("Uppercase:", repr(result_upper))
    print("Title Case:", repr(result_title))