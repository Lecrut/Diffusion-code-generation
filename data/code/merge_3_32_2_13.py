class StringAnalyzer:
    """A class that analyzes string properties."""

    def get_length(self, text):
        """Returns the length of the input string.

        Args:
            text (str): The string to measure.

        Returns:
            int: The number of characters in the string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        12345,  # This will cause a TypeError if passed directly to get_length without string conversion, 
               # but the class expects str. Let's ensure we pass strings in our test cases below.
    ]

    analyzer = StringAnalyzer()

    for sample in samples:
        try:
            length = analyzer.get_length(sample)
            print(f"Length of '{sample}' is {length}.")
        except TypeError as e:
            # Handle non-string input gracefully if needed, though spec implies string input.
            # Here we demonstrate robustness by converting or catching the error for specific test cases like '12345' 
            # which would naturally fail len() on a list/int without prior conversion logic in get_length itself.
            # However, strictly following Python's built-in str length behavior:
            print(f"Error measuring non-string input '{sample}': {e}")

    # Explicit string test for integer representation to show full capability if user passed int as text representation contextually? 
    # No, the task says compute length of INPUT STRING. So we assume valid strings in main logic flow unless specified otherwise.
    # Re-running specific known cases:
    
    print("\n--- Specific Test Cases ---")
    test_cases = [
        ("Empty string", ""),
        ("Single char", "a"),
        ("Multi-word sentence", "The quick brown fox jumps over the lazy dog."),
    ]

    for desc, text in test_cases:
        result = analyzer.get_length(text)
        print(f"{desc}: Length is {result}")