class StringAnalyzer:
    def get_length(self, text):
        """
        Computes and returns the length of the input string.

        Args:
            text (str): The input string to measure.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()

    sample_texts = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for text in sample_texts:
        length = analyzer.get_length(text)
        print(f"Length of '{text}': {length}")