class StringReverser:
    """A class providing utilities to reverse strings."""

    def reverse(self, text: str) -> str:
        """
        Reverses the input string efficiently using slice assignment logic compatible with Python's optimized slicing mechanism.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new reversed string.
        """
        return text[::-1]

if __name__ == '__main__':
    sample_strings = ["hello world", "Python is great"]

    for s in sample_strings:
        reverser = StringReverser()
        result = reverser.reverse(s)
        print(f"Original: {s}")
        print(f"Reversed:{result}\n")