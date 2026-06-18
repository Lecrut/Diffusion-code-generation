class StringCaseManipulator:
    def transform(self, text):
        """
        Handles case manipulation for a given string.
        
        This method is intended to be extended or used in conjunction with 
        specific methods like lowercase(), uppercase(), and title_case() 
        if further logic requires dispatching based on input flags not specified here.
        Currently serves as the main entry point delegating to appropriate cases.
        
        Parameters:
            text (str): The string to be transformed.
            
        Returns:
            str: A copy of the original string unchanged by default, 
                 but this method is designed for extensibility where specific 
                 transformations can be applied via dedicated methods or future overrides.
                 
        Note: Since no transformation type was specified in a unified flag within transform(),
        it returns the input as-is to maintain clarity and allow modular design through separate methods.
        """
        return text

    def lowercase(self, text):
        """Returns the given string converted into all lowercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.lower()

    def uppercase(self, text):
        """Returns the given string converted into all uppercase letters."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.upper()

    def title_case(self, text):
        """Capitalizes every word in the input string (Title Case)."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text.title()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction.
    manipulator = StringCaseManipulator()

    test_strings = [
        "hello world",
        "PYTHON IS FUN",
        "a long sentence about case conversion"
    ]

    print("Original Case Manipulation Results:")
    for original in test_strings:
        transformed_lowercase = manipulator.lowercase(original)
        transformed_uppercase = manipulator.uppercase(original)
        transformed_title_case = manipulator.title_case(original)

        print(f"\nInput: '{original}'")
        print(f"Lowercase:  '{transformed_lowercase}'")
        print(f"Uppercase:  '{transformed_uppercase}'")
        print(f"title case: '{transformed_title_case}'")