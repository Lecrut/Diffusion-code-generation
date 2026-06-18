class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string in place (modifies self) and returns it.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        # Using slicing for efficient reversal as per Python best practices
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_cases = [
        "Hello, World!",
        "",
        "Python",
        "A man a plan a canal Panama"
    ]

    reverser = StringReverser()

    for text in test_cases:
        reversed_text = reverser.reverse(text)
        print(f"Original: '{text}'")
        print(f"Reversed: '{reversed_text}'\n")