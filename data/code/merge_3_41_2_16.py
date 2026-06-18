class StringCaseManipulator:
    """A class to handle case manipulation operations on strings."""

    def transform(self, text):
        """
        Transforms the given string based on available methods (lowercase, uppercase, title).
        
        Since this method is intended as a general transformer but specific cases 
        require separate implementations per requirement clarity, we will return None 
        here and delegate to dedicated methods. In an extended scenario without explicit 
        transformation type input, this serves as a placeholder or could raise an error 
        indicating the need for a mode parameter if dynamic behavior were required.
        
        However, adhering strictly to the task of providing separate methods while keeping 
        'transform' functional: we will assume it should apply Title Case by default 
        unless overridden internally, but per strict separation instructions below, 
        this method is kept minimal and delegates logic conceptually or raises if mode isn't specified.
        
        To satisfy runnable standalone behavior with clear usage patterns as implied:
        We'll make transform call title_case() by default for backward compatibility in examples.
        """
        return self.title_case(text)

    def lowercase(self, text):
        """Converts the input string to all lowercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.lower()

    def uppercase(self, text):
        """Converts the input string to all uppercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.upper()

    def title_case(self, text):
        """Converts the first letter of each word to uppercase and the rest to lowercase."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        # Using standard Python's built-in for robustness (handles multiple spaces correctly)
        return text.title()

if __name__ == '__main__':
    manipulator = StringCaseManipulator()

    sample_text = "hello world this is python"

    print("Original Text:", sample_text)
    
    lower_result = manipulator.lowercase(sample_text)
    print("Lowercase Result:", lower_result)

    upper_result = manipulator.uppercase(sample_text)
    print("Uppercase Result:", upper_result)

    title_result = manipulator.title_case(sample_text)
    print("Title Case Result:", title_result)

    # Using the transform method which defaults to title_case for demonstration consistency
    transformed_via_method = manipulator.transform(sample_text)
    print("Transform Method (Default Title):", transformed_via_method)