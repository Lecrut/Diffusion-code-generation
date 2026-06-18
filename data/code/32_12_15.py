class StringAnalyzer:
    """A clean class designed to analyze basic properties of strings."""

    def get_length(self, text) -> int:
        """Calculates and returns the length of the input string.
        
        Args:
            text (str): The string for which the length is calculated.
            
        Returns:
            int: The number of characters in the provided string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    
    analyzer = StringAnalyzer()
    
    test_cases = [
        ("Hello, World!", 13),
        (0, "not a string"),
        ("", 0),
        ("Python is powerful and clean.", 29)
    ]

    for input_text, expected_length in test_cases:
        result = analyzer.get_length(input_text if isinstance(input_text, str) else "")
        
        # Handle the special case where a non-string integer was passed as sample data logic needs to be robust. 
        # Since '0' is an int but we expect string length, let's ensure input conversion for safety in analysis context or treat it based on strict typing.
        # The task implies `text` is str, so passing 0 would fail type expectation strictly, but len() works on any sequence-like object if we wanted to be generic. 
        # However, the method signature expects text (str). Let's process safely for demonstration.

        final_input = input_text
        try:
            length = analyzer.get_length(final_input)
            
            status = "PASS" if length == expected_length else f"FAIL (Got {length})"
            
            print(f"Input: '{final_input}' -> Length: {length} [{status}]")
        except Exception as e:
            # If a non-string was passed directly without conversion logic inside the class, it would raise TypeError.
            # The sample includes '0' to test boundary or type robustness if not strictly typed at runtime check level. 
            # We will assume standard usage where input is str.
            status = f"Exception: {e}"
        finally:
             print(f"Result for case '{expected_length}': {status}")

    # Explicit run with a clean string to guarantee success output without errors on the '0' int if strict typing holds 
    # or just ignore the float/int in sample list by casting during logic flow inside main block.
    
    raw_samples = ["", "a", "ab"]
    print("\nRunning specific simple samples:")
    for s in raw_samples:
        l = analyzer.get_length(s)
        print(f"String '{s}' has length {l}")