class StringCaseManipulator:
    """A class to handle case manipulation of strings."""

    def transform(self, text):
        """
        Handles case manipulation for a given string based on internal state or method calls.
        
        This method is designed as the primary interface but currently acts as a dispatcher 
        since specific transformation methods (lowercase, uppercase, title) are separate.
        In this implementation, it defaults to returning the input text unchanged unless 
        overridden by calling instance-specific methods directly for clarity and modularity.
        
        Note: To demonstrate functionality without an explicit 'mode' argument in transform(),
        we will have callers invoke specific helper methods (e.g., self.lowercase()).
        This method serves as a placeholder or can be extended to accept a mode parameter 
        if needed, but the task specifies separate methods.
        
        Args:
            text (str): The input string to potentially process.
            
        Returns:
            str: The original text since specific transformations are handled by dedicated methods.
        """
        return text

    def lowercase(self, text):
        """Converts the given text to all lowercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.lower()

    def uppercase(self, text):
        """Converts the given text to all uppercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.upper()

    def title_case(self, text):
        """Capitalizes each word in the given text (Title Case)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        # Using Python's built-in capitalize logic adapted for words. 
        # Note: The standard 'title()' method handles this well but may behave differently with punctuation depending on locale/settings in some environments.
        return text.title()

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    
    manipulator = StringCaseManipulator()

    test_string = "hello world! this is a python class."

    print("Original Text:")
    print(test_string)
    
    result_lower = manipulator.lowercase(test_string)
    print("\nLowercase Transformation:")
    print(result_lower)
    
    result_upper = manipulator.uppercase(test_string)
    print("\nUppercase Transformation:")
    print(result_upper)
    
    result_title = manipulator.title_case(test_string)
    print("\nTitle Case Transformation:")
    print(result_title)

    # Demonstrate the transform method behavior (currently returns original as per design logic above)
    result_transform = manipulator.transform(test_string)
    print("\nTransform Method Output (Default):")
    print(result_transform)