class StringCaseManipulator:
    def transform(self, text):
        """
        Handles case manipulation for a given string.
        
        This method acts as a dispatcher to other specific case transformation methods.
        It currently returns the original text with no transformation applied by default,
        but is designed to be extended or overridden in subclasses if needed.
        
        Note: Since this class does not accept a 'method' parameter for dynamic behavior 
        based on external input (to avoid interactive prompts), it defaults to returning 
        the string unchanged unless specific methods are called directly via other means.
        
        Args:
            text (str): The input string to be processed.
            
        Returns:
            str: The original input string as no transformation is defined in this base method.
                 Users should call lowercase(), uppercase(), or title_case() for actual transformations.
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
        # Python's built-in capitalize only affects the first character. 
        # We use split and join to achieve true title case for multiple words.
        return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    manipulator = StringCaseManipulator()

    sample_text = "hello world this is a test string"

    # Demonstrate lowercase transformation
    result_lower = manipulator.lowercase(sample_text)
    
    # Demonstrate uppercase transformation
    result_upper = manipulator.uppercase(sample_text)
    
    # Demonstrate title case transformation
    result_title = manipulator.title_case(sample_text)

    print("Original:", sample_text)
    print("Lowercase:", result_lower)
    print("Uppercase:", result_upper)
    print("Title Case:", result_title)