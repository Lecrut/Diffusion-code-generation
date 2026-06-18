class StringReverser:
    """A class that provides utility methods to reverse strings."""

    def __init__(self):
        self._instance_data = None  # Placeholder for future expansion if needed

    def reverse(self, text: str) -> str:
        """
        Reverses the input string.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new string that is the reverse of the input.
        """
        return text[::-1]

if __name__ == '__main__':
    # Create an instance of StringReverser with hard-coded sample values
    reverser = StringReverser()

    samples = [
        "Hello, World!",
        "Python Programming",
        "1234567890",
        ""  # Edge case: empty string
    ]

    for text in samples:
        reversed_text = reverser.reverse(text)
        print(f"Original: '{text}'")
        print(f"Reversed: '{reversed_text}'\n")