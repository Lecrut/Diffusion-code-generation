class StringReverser:
    """A class that provides utility methods to reverse strings."""

    def reverse(self, text):
        """
        Reverses a given string in place and returns it.

        Args:
            text (str): The input string to be reversed.

        Returns:
            str: The reversed string.
        
        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    test_cases = [
        "hello world",
        "Python programming",
        "",
        "A"
    ]

    reverser = StringReverser()

    for text in test_cases:
        reversed_text = reverser.reverse(text)
        print(f"Original: '{text}'")
        print(f"Reversed: '{reversed_text}'\n")