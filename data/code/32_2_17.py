class StringAnalyzer:
    """A class to analyze string properties."""

    def get_length(self, text):
        """Returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    # Sample values - no user interaction or external dependencies required.
    analyzer = StringAnalyzer()
    
    sample_texts = [
        "Hello",
        "",
        "Python is great!",
        12345,  # Should handle non-string inputs gracefully if applicable, 
               # but per Python's len(), it raises TypeError for numbers.
                          # Since the task asks to compute length of input string, 
                          # we assume valid strings in this context or let built-in behavior stand.
    ]

    print("String Analysis Results:")
    for text in sample_texts:
        try:
            length = analyzer.get_length(text) if isinstance(text, str) else len(str(text))
            print(f"Input: {repr(text)} -> Length: {length}")
        except TypeError as e:
            print(f"Error processing input {type(text).__name__}: {e}")