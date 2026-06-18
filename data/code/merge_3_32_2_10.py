class StringAnalyzer:
    """A class to analyze string properties."""

    def get_length(self, text):
        """
        Computes and returns the length of the input string.

        Args:
            text (str): The input string whose length is to be calculated.

        Returns:
            int: The number of characters in the input string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "Hello, World!",
        "",
        "Python 3",
        "a" * 100
    ]

    analyzer = StringAnalyzer()

    print("String Length Analysis Results:")
    for text in samples:
        length = analyzer.get_length(text)
        print(f"'{text}' -> Length: {length}")