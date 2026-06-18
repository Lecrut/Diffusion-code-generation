class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses a given string.

        Args:
            text (str): The input string to be reversed.

        Returns:
            str: The reversed string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "A single character 'a'",
        "Race car"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for original in test_cases:
        reversed_str = reverser.reverse(original)
        print(f'Original:  "{original}"')
        print(f'Reversed:  "{reversed_str}"\n')