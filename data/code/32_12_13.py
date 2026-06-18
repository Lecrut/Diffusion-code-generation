class StringAnalyzer:
    def get_length(self, text):
        """Calculates and returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Sample test cases with hard-coded values
    samples = [
        "Hello World",
        "",
        "Python Programming",
        123,
        None
    ]

    for sample in samples:
        try:
            length = analyzer.get_length(sample) if isinstance(sample, str) else None
            print(f"Input: {repr(sample)} -> Length: {length}")
        except Exception as e:
            # Handle non-string inputs gracefully by returning None or raising specific error logic if needed
            pass