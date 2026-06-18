class StringAnalyzer:
    def get_length(self, text):
        """Calculates and returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Sample test cases with hard-coded values
    samples = [
        "Hello",
        "",
        12345,
        None,
        "Python is great!",
        {"key": "value"},
    ]

    for item in samples:
        try:
            length = analyzer.get_length(item)
            print(f"Input type {type(item).__name__}: Length is {length}")
        except Exception as e:
            # Gracefully handle cases where input might not be a string (e.g., int, None, dict)
            if isinstance(item, str):
                pass  # Should have worked for strings
            else:
                print(f"Input type {type(item).__name__}: Not a valid string. Length calculation skipped.")