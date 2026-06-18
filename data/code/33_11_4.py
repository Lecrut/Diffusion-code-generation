class StringCleaner:
    """A class to clean strings by removing spaces efficiently."""

    def clean(self, text):
        """
        Removes all space characters from the input string.

        Args:
            text (str): The input string containing potential spaces.

        Returns:
            str: A new string with all spaces removed.
        
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string type, got {type(text).__name__}")
        
        # Using replace() which is highly optimized in CPython for simple character replacement
        return text.replace(' ', '')

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "Hello World",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesHere",
        "  Leading and Trailing spaces  ",
        "\t\tTabs are not removed (only space char)",
        "Mixed: a b c d e f g h i j k l m n o p q r s t u v w x y z"
    ]

    cleaner = StringCleaner()

    print("String Cleaner Test Results:")
    for original in test_cases:
        cleaned = cleaner.clean(original)
        status = "OK" if ' ' not in cleaned else "FAIL (spaces remain)"
        print(f"Input: {repr(original)}")
        print(f"Output: {repr(cleaned)} - Status: {status}")
        print("-" * 40)