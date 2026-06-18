class StringAnalyzer:
    """A class designed to analyze string properties."""

    def get_length(self, text):
        """Returns the length of the input string.

        Args:
            text (str): The string whose length is to be calculated.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    analyzer = StringAnalyzer()

    sample_texts = [
        "Hello, World!",
        "",
        "Python is awesome",
        "12345"
    ]

    for text in sample_texts:
        length = analyzer.get_length(text)
        print(f"'{text}' has a length of {length}.")