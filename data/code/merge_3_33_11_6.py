class StringCleaner:
    """A class to clean strings by removing all spaces."""

    def clean(self, text: str) -> str:
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
            raise TypeError(f"Expected string type but got {type(text).__name__}")

        # Using join on list comprehension for optimized space removal in Python 3+
        return ''.join(char for char in text if char != ' ')

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "Hello World",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesHere!",
        "Python 3.12 is great.",
    ]

    cleaner = StringCleaner()
    
    for i, original_text in enumerate(test_cases):
        cleaned_text = cleaner.clean(original_text)
        print(f"Input: {repr(original_text)}")
        print(f"Output: {repr(cleaned_text)}")
        if original_text == "":
            assert cleaned_text == "", "Empty string should remain empty."
        else:
            # Verify no spaces exist in the output for non-empty inputs
            assert ' ' not in cleaned_text, "Spaces found in cleaned text!"
        
        print("-" * 40)