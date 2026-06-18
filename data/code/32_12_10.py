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
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        "Hello, World!",
        "",
        "Python is great.",
        "12345",
        "!@#$%^&*()"
    ]

    analyzer = StringAnalyzer()

    print("String Length Analysis Results:")
    for sample in samples:
        length = analyzer.get_length(sample)
        print(f"Input: '{sample}' -> Length: {length}")