class StringAnalyzer:
    """A class to analyze string properties."""

    def get_length(self, text):
        """Returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Sample test cases with hard-coded values
    samples = [
        "Hello World",
        "",
        123,      # Non-string input to demonstrate potential error handling context (though len accepts it)
        "Python is great!",
        "   spaced string   ",
        "\n\t\n"
    ]

    for sample in samples:
        try:
            length = analyzer.get_length(sample)
            print(f"Input repr: {repr(sample):20} | Length: {length}")
        except Exception as e:
            print(f"Error processing input of type {type(sample).__name__}: {e}")