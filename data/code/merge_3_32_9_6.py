"""Utility module containing a static method to calculate string length."""

class StringUtilities:
    """A utility class providing helper methods for string operations."""

    @staticmethod
    def get_length(text: str) -> int:
        """
        Calculate the number of characters in the given text.

        Args:
            text (str): The input string to measure.

        Returns:
            int: The length of the string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction.
    samples = [
        "Hello, World!",
        "",
        "Python 3.x",
        "a" * 1000,
    ]

    print("String Length Calculation Results:")
    for text in samples:
        length = StringUtilities.get_length(text)
        print(f"'{text[:20]}...' (length {len(text)}) -> Calculated: {length}")