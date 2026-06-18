class StringReverser:
    """A class that provides functionality to reverse strings."""

    def reverse(self, text):
        """
        Reverses the input string.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new string which is the reverse of the input.
        """
        return text[::-1]

if __name__ == '__main__':
    # Sample values - no user input or command-line arguments required
    sample_strings = [
        "Hello, World!",
        "Python Programming",
        "",
        "A man a plan a canal Panama"
    ]

    reverser = StringReverser()

    for original in sample_strings:
        reversed_text = reverser.reverse(original)
        print(f"Original:  '{original}'")
        print("Reversed:  '" + reversed_text + "'\n")