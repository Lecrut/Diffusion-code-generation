class StringAnalyzer:
    def get_length(self, text):
        """Returns the length of the input string."""
        return len(text)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    # Sample test cases with hard-coded values
    sample_texts = [
        "Hello",
        "",
        "Python is great!",
        12345,  # Should work if text accepts non-string or just returns len of str representation depending on implementation. 
               # However, strictly for string length per task description:
               # We will pass strings only to ensure correctness as per 'length of input string' requirement.
    ]

    print("StringAnalyzer Test Results:")
    for test_input in sample_texts:
        if isinstance(test_input, str):
            result = analyzer.get_length(test_input)
            print(f"Input: {test_input!r} -> Length: {result}")
        else:
            # Fallback to string representation length just in case non-string is passed unexpectedly by user logic elsewhere
            try:
                result = len(str(test_input))
                print(f"Input: {test_input!r} (converted) -> Length: {result}")
            except Exception as e:
                print(f"Error processing input {test_input}: {e}")