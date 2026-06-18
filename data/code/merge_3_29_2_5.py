class StringReverser:
    """A class designed to reverse strings."""

    def reverse(self, word):
        """
        Reverses the input string in-place if it is a list of characters,
        or returns a new reversed string for standard strings.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: A new string with the characters of 'word' in reverse order.
        """
        return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "hello",
        "Python programming",
        "",
        "a" * 10,
        "!@#$%"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for word in test_cases:
        reversed_word = reverser.reverse(word)
        # Using f-string formatting to ensure no markdown is rendered outside the code block logic
        result_line = f"Original: '{word}' -> Reversed: '{reversed_word}'"
        print(result_line)