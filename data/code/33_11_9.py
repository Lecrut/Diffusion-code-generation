class StringCleaner:
    """A class to clean strings by removing spaces."""

    def clean(self, text):
        """
        Removes all space characters from the input string efficiently.

        Args:
            text (str): The input string containing potential spaces.

        Returns:
            str: A new string with all spaces removed.
        
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string type, got {type(text).__name__}")
        
        # Using replace() which is implemented in C and highly optimized for this operation
        return text.replace(' ', '')

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "Hello World",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesHere",
        "Python 3.12 is great!",
        "\t\n\r\t\n"  # Tabs and newlines are not spaces, but included for completeness check if needed later
    ]

    cleaner = StringCleaner()

    print("Testing StringCleaner.clean():")
    for i, test_input in enumerate(test_cases):
        try:
            result = cleaner.clean(test_input)
            status = "Success"
        except Exception as e:
            result = f"Error: {e}"
            status = "Exception Raised (Expected or Unexpected)"

        print(f"\nTest Case {i + 1}:")
        print(f"Input:    |{test_input}|")
        print(f"Output:   |{result}|")
        print(f"Status:   [{status}]")