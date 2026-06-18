class StringAnalyzer:
    """A utility class for analyzing string properties."""

    def get_length(self, text):
        """
        Calculates and returns the length of the input string.

        Args:
            text (str): The string to analyze.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "Hello, World!",
        "",
        "Python is great.",
        1234567890 * "" + str(1234567890),  # String representation of a number
    ]

    analyzer = StringAnalyzer()

    for sample in samples:
        length = analyzer.get_length(sample)
        print(f"Length of '{sample}' is {length}.")