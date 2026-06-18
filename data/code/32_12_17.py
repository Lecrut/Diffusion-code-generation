class StringAnalyzer:
    def get_length(self, text):
        """Calculates and returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Sample test cases with hard-coded values
    test_strings = [
        "Hello, World!",
        "",
        "Python is awesome",
        1234567890 * ""  # Empty string from multiplication (edge case for type hinting)
    ]

    print("String Length Analysis Results:")
    for test_str in test_strings:
        length = analyzer.get_length(test_str)
        if isinstance(test_str, str):
            print(f"Input '{test_str}' -> Length: {length}")
        else:
            # Handle edge case where text might not be a string (though type hint implies otherwise)
            try:
                result_len = len(str(test_str))
                print(f"Non-string input converted to str, Input repr '{repr(test_str)}' -> String Length: {result_len}")
            except Exception as e:
                print(f"Error processing non-string input '{test_str}': {e}")