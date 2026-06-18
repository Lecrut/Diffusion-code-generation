class StringReverser:
    """A class designed to reverse strings efficiently using object-oriented principles."""

    def __init__(self):
        """Initialize a new instance of the StringReverser class without arguments."""
        pass

    def reverse(self, text: str) -> str:
        """Returns the reversed version of the input string.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new string with characters in reverse order.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes only.
    test_cases = [
        "hello",
        "Python is great!",
        "",
        "A man a plan a canal Panama!"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for original in test_cases:
        reversed_text = reverser.reverse(original)
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_text}'\n")