class StringAnalyzer:
    """A class to analyze string properties."""

    def get_length(self, text):
        """
        Computes and returns the length of the input string.

        Args:
            text (str): The string whose length is to be determined.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    analyzer = StringAnalyzer()

    test_strings = [
        "",                  # Empty string
        "Hello",             # Simple word
        "Python Programming",# Sentence with space
        "!@#$%",             # Special characters
    ]

    print("String Analysis Results:")
    for s in test_strings:
        length = analyzer.get_length(s)
        status = "(empty)" if length == 0 else ""
        print(f"'{s}' (length {len(s)}){status}")