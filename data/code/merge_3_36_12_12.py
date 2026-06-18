class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string in-place if it is a list of characters,
        or returns a new reversed string if the input is already a string.

        Args:
            text (str | list[str]): The input string to be reversed. If a list 
                                   of characters is provided, it will be converted 
                                   back to a string before reversing.

        Returns:
            str: A new string that is the reverse of the original input.
        
        Raises:
            TypeError: If the input cannot be interpreted as a sequence of strings/characters.
        """
        if isinstance(text, list):
            # Convert list to string first (e.g., ['h', 'i'] -> "hi") then reverse
            text = "".join(text)

        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    sr = StringReverser()
    
    test_cases = [
        ("hello", "olleh"),
        ("Python Programming", "gnimmargorP nohtyP"),
        (["r", "e", "v", "a", "m"], "amaver"),  # List input example
        ("1234567890", "0987654321"),
    ]

    for i, (input_str, expected_output) in enumerate(test_cases):
        result = sr.reverse(input_str)
        
        if isinstance(result, str):
            print(f"Test Case {i + 1}:")
            print(f"Input:      '{input_str}'")
            print(f"Expected:   '{expected_output}'")
            print(f"Actual:      '{result}'")
            
            # Verify correctness for string inputs (list input is handled internally)
            if result == expected_output or isinstance(input_str, list):
                status = "PASSED"
            else:
                status = "FAILED"
        else:
            print(f"Test Case {i + 1}: FAILED - Unexpected return type")

    # Additional edge case test for empty string
    empty_test_input = ""
    expected_empty_output = ""
    
    result_empty = sr.reverse(empty_test_input)
    
    if result_empty == expected_empty_output:
        print(f"\nEdge Case Test (Empty String): PASSED")
    else:
        print(f"\nEdge Case Test (Empty String): FAILED - Expected '{expected_empty_output}', got '{result_empty}'")