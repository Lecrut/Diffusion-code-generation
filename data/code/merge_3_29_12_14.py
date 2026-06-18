class StringReverser:
    """A class designed to reverse strings efficiently."""

    def reverse(self, text: str) -> str:
        """
        Reverses the input string in-place and returns it as a new string.
        
        Args:
            text (str): The string to be reversed.
            
        Returns:
            str: A new string with characters in reverse order.
        """
        return ''.join(reversed(text))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "",
        "A",
        "Python is awesome.",
        12345  # Note: This will fail if passed directly as int; assuming string context per task description. 
             # Adjusted to ensure valid input type for the method signature defined above.
    ]

    sample_strings = [
        "Hello, World!",
        "",
        "A",
        "Python is awesome."
    ]

    print("Testing StringReverser class:")
    
    for s in sample_strings:
        reverser = StringReverser()
        reversed_s = reverser.reverse(s)
        print(f"Original: '{s}'")
        print(f"Reversed: '{reversed_s}'\n")