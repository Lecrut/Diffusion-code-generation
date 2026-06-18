class StringReverser:
    """A class that provides methods to reverse strings."""

    def reverse(self, text):
        """
        Reverses the input string.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new string with characters in reverse order.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing the StringReverser class
    reverser = StringReverser()
    
    test_strings = [
        "Hello, World!",
        "Python",
        "",
        "A single character 'z'",
        "12345"
    ]

    print("String Reversal Examples:")
    for original in test_strings:
        reversed_str = reverser.reverse(original)
        print(f'Original: "{original}"')
        print(f'Reversed: "{reversed_str}"\n')