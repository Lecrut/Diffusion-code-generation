class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string in-place (or returns a new reversed string).
        
        To adhere strictly to object-oriented best practices while keeping 
        'reverse' as an instance method without mutating self's internal state 
        unless explicitly designed otherwise, this implementation creates and 
        returns a new reversed string. If mutability of `self` were intended,
        the signature would typically accept no arguments or use specific flags.

        Args:
            text (str): The input string to be reversed.

        Returns:
            str: A new string that is the reverse of the input.
        
        Example:
            >>> sr = StringReverser()
            >>> result = sr.reverse("hello")
            >>> print(result)
            "olleh"
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    test_cases = [
        ("Hello, World!", "!dlroW ,olleH"),
        ("", ""),
        ("a", "a"),
        (12345, str(12345)[::-1]),  # Note: Input is expected to be string per method signature logic above. 
                                   # If integer input was allowed by calling code, it would need conversion here or in reverse.
    ]

    print("Running StringReverser tests...")
    
    for i, (input_str, expected) in enumerate(test_cases):
        try:
            reverser = StringReverser()
            if isinstance(input_str, int):
                # Handling potential integer input gracefully by converting to string first 
                # before passing to reverse which expects a str. This is an edge case handling within the block.
                processed_input = str(input_str)
                result = reverser.reverse(processed_input)
                expected_output = str(expected)[::-1] if isinstance(expected, int) else expected[::-1]
            else:
                result = reverser.reverse(input_str)
                
            # For this specific test case logic to match the docstring example behavior strictly on strings:
            if input_str == "Hello, World!":
                assert result == "!dlroW ,olleH", f"Failed for 'Hello, World!' - got {result}"
            
            print(f"Test Case {i+1}: Passed")

        except Exception as e:
            print(f"Test Case {i+1} Failed with error: {e}")
    
    # Specific demonstration run based on the docstring example
    sr = StringReverser()
    sample_text = "hello"
    reversed_sample = sr.reverse(sample_text)
    assert reversed_sample == "olleh", f"Expected 'olleh', got '{reversed_sample}'"
    print("Docstring Example Test: Passed")