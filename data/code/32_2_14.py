import string

class StringAnalyzer:
    """A class for analyzing strings with various metrics."""

    def get_length(self, text):
        """Returns the length of the input string.

        Args:
            text (str): The string to analyze.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()

    # Hard-coded sample values ensuring no user input, network access, or files are required.
    samples = [
        "Hello",
        "",
        "Python is great!",
        1234567890 * "" + "A"  # Just to test with empty string multiplication logic if needed, but here it's just a long string concept. 
                              # Actually simpler: A very long repeated character sequence.
    ]

    for text in samples:
        length = analyzer.get_length(text)
        print(f"'{text}' has length {length}")