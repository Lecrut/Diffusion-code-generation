class StringAnalyzer:
    """A class designed to analyze string properties."""

    def get_length(self, text):
        """Calculates and returns the length of the input string.

        Args:
            text (str): The string whose length is to be calculated.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    samples = [
        "Hello, World!",
        "",
        "Python is awesome",
        "12345"
    ]

    analyzer = StringAnalyzer()

    print("String Length Analysis Results:")
    for text in samples:
        length = analyzer.get_length(text)
        print(f"'{text}' has a length of {length}.")