class StringAnalyzer:
    """A clean object-oriented class to analyze basic string properties."""

    def get_length(self, text):
        """Returns the length of the input string as an integer."""
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies.
    samples = [
        "Hello World",
        "",
        12345,
        None,
    ]

    analyzer = StringAnalyzer()

    print("String Analysis Results:")
    for item in samples:
        try:
            length = analyzer.get_length(item) if isinstance(item, str) else "Not a string"
            print(f"'{item}' -> Length: {length}")
        except Exception as e:
            # Gracefully handle non-string inputs that aren't explicitly handled by the logic above.
            print(f"Input '{item}' raised an error (expected for non-strings): {e}")