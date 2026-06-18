class StringAnalyzer:
    """A class designed to analyze string properties."""

    def get_length(self, text):
        """Calculates and returns the length of the input string.

        Args:
            text (str): The string whose length is to be calculated.

        Returns:
            int: The number of characters in the provided string.
        """
        return len(text)

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample_texts = [
        "Hello, World!",
        "",
        "Python is great.",
        "A" * 1000
    ]

    analyzer = StringAnalyzer()

    print("String Analysis Results:")
    for text in sample_texts:
        length = analyzer.get_length(text)
        print(f"'{text}' has a length of {length}.")