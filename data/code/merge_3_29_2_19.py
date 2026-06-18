class StringReverser:
    """A class that provides utilities to reverse strings."""

    def __init__(self):
        """Initialize the StringReverser instance with no arguments needed."""
        pass

    def reverse(self, word: str) -> str:
        """Reverse the input string.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # No user input, command-line arguments, or network access is required.
    
    reverse = StringReverser()

    test_strings = [
        "Hello World",
        "Python Programming",
        "",
        "a"
    ]

    print("String Reversal Results:")
    for original in test_strings:
        reversed_str = reverse.reverse(original)
        # Output format ensures readability even if input is None or empty logic holds.
        # In this case, inputs are valid strings as per the requirement that no user input happens at runtime.
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")