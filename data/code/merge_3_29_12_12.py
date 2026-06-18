class StringReverser:
    """A class designed to reverse strings efficiently."""

    def __init__(self, text: str = "") -> None:
        """Initialize the StringReverser with an optional string."""
        self._original_text = text

    @staticmethod
    def reverse(text: str) -> str:
        """Reverse a given string using slicing for efficiency.

        Args:
            text (str): The input string to be reversed.

        Returns:
            str: A new string containing the characters of the original string in reverse order.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "",
        "Python 3.9",
        "A man a plan a canal Panama!"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for original in test_cases:
        reversed_str = reverser.reverse(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_str}'\n")