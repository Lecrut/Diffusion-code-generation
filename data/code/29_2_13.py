class StringReverser:
    """A class to reverse strings."""

    def reverse(self, word):
        """
        Reverses the input string in place using a list of characters and then joins it back into a string.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        # Convert string to a list for mutability, reverse the list, join elements back together
        return ''.join(list(word)[::-1])

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or command-line args)
    test_cases = [
        "Hello",
        "Python Programming",
        "",
        "A"
    ]

    reverser = StringReverser()

    for word in test_cases:
        reversed_word = reverser.reverse(word)
        print(f'Original: "{word}" -> Reversed: "{reversed_word}"')