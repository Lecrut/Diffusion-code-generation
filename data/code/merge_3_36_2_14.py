class StringReverser:
    """A class providing string manipulation services with a focus on reversal."""

    def reverse(self, text):
        """
        Reverses the input string.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new string containing characters in reverse order.
        
        Examples:
            >>> reverser = StringReverser()
            >>> reverser.reverse("hello")
            "olleh"
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = ["Hello, World!", 1234567890, "", "Python is great", "!tsir"]

    reverser = StringReverser()

    for text in test_cases:
        result = reverser.reverse(text)
        print(f"Original: '{text}'")
        print(f"Reversed: '{result}'\n")