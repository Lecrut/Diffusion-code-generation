class StringCleaner:
    """A class to clean strings by removing all spaces."""

    def clean(self, text):
        """
        Removes all space characters from the input string efficiently.

        Args:
            text (str): The input string potentially containing spaces.

        Returns:
            str: A new string with all spaces removed.
        
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string type, got {type(text).__name__}")
        
        # In Python 3.12+, 'text.replace(' ', '')' is highly optimized in CPython 
        # because it's implemented in C and handles the iteration efficiently.
        return text.replace(" ", "")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input
    
    test_cases = [
        "Hello, World!",           # Normal case with one space
        "...",                     # String full of spaces (edge case)
        "",                       # Empty string edge case
        "NoSpacesHere",            # No spaces present
        "  Leading and Trailing   ",# Multiple leading/trailing spaces
    ]

    cleaner = StringCleaner()

    for i, original_text in enumerate(test_cases):
        cleaned_text = cleaner.clean(original_text)
        print(f"Test Case {i + 1}:")
        print(f"Input:    '{original_text}'")
        print(f"Output:   '{cleaned_text}'")
        print("-" * 30)