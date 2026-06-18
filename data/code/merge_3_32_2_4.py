class StringAnalyzer:
    """A class to analyze string properties."""

    def get_length(self, text):
        """
        Computes and returns the length of the input string.

        Args:
            text (str): The string whose length is to be computed.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    analyzer = StringAnalyzer()
    
    test_cases = [
        "Hello, World!",
        "",
        "Python",
        1234567890 * "a"  # A long string to ensure robustness
    ]

    for text in test_cases:
        length = analyzer.get_length(text)
        print(f"'{text}' has a length of {length}.")