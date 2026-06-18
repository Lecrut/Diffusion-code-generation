class StringAnalyzer:
    """A class to analyze string properties."""

    def get_length(self, text):
        """
        Computes and returns the length of the input string.

        Args:
            text (str): The string whose length is to be computed.

        Returns:
            int: The number of characters in the string.
        
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected type 'str', got {type(text).__name__}")
        
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    analyzer = StringAnalyzer()

    test_strings = [
        "Hello, World!",
        "",
        "Python 3.10",
        None,  # This will trigger a TypeError demonstration if tested directly (though usually not run)
    ]

    for s in test_strings:
        try:
            length = analyzer.get_length(s)
            print(f"Length of '{s}' is {length}")
        except Exception as e:
            print(f"Error processing input: {e}")