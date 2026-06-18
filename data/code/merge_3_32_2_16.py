class StringAnalyzer:
    def get_length(self, text):
        """
        Computes and returns the length of the input string.
        
        Args:
            text (str): The input string to analyze.
            
        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()

    # Sample test cases with hard-coded values
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        1234567890 * "\n",  # A string of newlines (length matches integer value)
    ]

    for sample in samples:
        length = analyzer.get_length(sample)
        print(f"Input: '{sample[:10]}...' if len > 10 else '{sample}'")
        print(f"Length: {length}\n")