class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, word):
        """
        Reverses the input string in-place (modifies self) and returns it.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        return "".join(reversed(word))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "hello",
        "Python Programming",
        "",
        "a"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for word in test_cases:
        reversed_word = reverser.reverse(word)
        print(f'Original: "{word}" -> Reversed: "{reversed_word}"')