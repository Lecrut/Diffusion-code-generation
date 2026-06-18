class StringAnalyzer:
    def get_length(self, text):
        """Returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Sample test cases with hard-coded values
    samples = [
        "Hello, World!",
        "",
        "Python",
        1234567890 * "a"  # A long string of repeated characters for stress testing
    ]

    print("String Analysis Results:")
    for sample in samples:
        length = analyzer.get_length(sample)
        print(f"'{sample[:10]}{'...' if len(sample) > 10 else ''}' -> Length: {length}")