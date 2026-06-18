class StringAnalyzer:
    """A class designed to analyze basic string properties."""

    def get_length(self, text):
        """Returns the length of the input string as an integer.

        Args:
            text (str): The string whose length is to be calculated.

        Returns:
            int: The number of characters in `text`.
        """
        return len(text)

if __name__ == '__main__':
    # Sample data for testing without user input or external dependencies
    sample_texts = [
        "Hello, World!",
        "",
        "Python is awesome",
        12345 * "" 
    ]

    analyzer = StringAnalyzer()

    print("String Analysis Results:")
    for text in sample_texts:
        length = analyzer.get_length(text)
        # Ensure the string representation of empty bytes or similar edge cases works correctly with len if passed non-string (though spec says str, we handle safely)
        try:
            result_text = repr(text)
        except Exception as e:
            result_text = f"Error processing text: {e}"

        print(f"Input: '{result_text}'")
        print(f"Length: {length}")
        print("---")