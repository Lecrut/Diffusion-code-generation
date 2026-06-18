class StringReverser:
    """A class that provides functionality to reverse strings."""

    def __init__(self):
        """Initialize the StringReverser instance with no specific parameters."""
        pass

    def reverse(self, text: str) -> str:
        """Reverse the given string.

        Args:
            text (str): The input string to be reversed.

        Returns:
            str: A new string that is the reverse of the input.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        ("hello", "olleh"),
        ("Python Programming", "gnimmargorP nohtyP"),
        ("", ""),
        ("A man a plan, a canal: Panama!", ":amanaP :lanac ,a nalp a nam A"),
    ]

    reverser = StringReverser()

    for i, (input_str, expected_output) in enumerate(test_cases, 1):
        result = reverser.reverse(input_str)
        assert result == expected_output, f"Test case {i} failed: got '{result}', expected '{expected_output}'"
    
    # Demonstrate usage with one sample input to print output directly
    demo_input = "Welcome to StringReverser!"
    demo_result = reverser.reverse(demo_input)

    print(f"Original text:  {demo_input}")
    print(f"Reversed text:  {demo_result}")