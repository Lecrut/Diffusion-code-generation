class StringAnalyzer:
    """A class to analyze string properties."""

    def get_length(self, text):
        """
        Computes and returns the length of the input string.

        Args:
            text (str): The input string whose length is to be computed.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    sample_texts = ["Hello", "Python Programming", "", "The quick brown fox"]
    
    for text in sample_texts:
        length = analyzer.get_length(text)
        print(f"Text: '{text}', Length: {length}")