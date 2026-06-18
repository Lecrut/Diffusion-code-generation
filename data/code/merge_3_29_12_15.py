class StringReverser:
    """A class that provides methods to reverse strings efficiently."""

    def reverse(self, text: str) -> str:
        """
        Reverses the input string in-place and returns it.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        # Efficient reversal using slice notation which is optimized in CPython
        return text[::-1]

if __name__ == '__main__':
    test_cases = [
        "Hello, World!",
        "",
        "a",
        "To be or not to be"
    ]

    reverser = StringReverser()

    for test_string in test_cases:
        reversed_result = reverser.reverse(test_string)
        print(f"Original: '{test_string}'")
        print(f"Reversed: '{reversed_result}'")
        print("-" * 20)