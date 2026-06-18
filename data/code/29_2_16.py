class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, word):
        """
        Reverses the input string.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: A new string with characters in reverse order.
        """
        return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    reverser = StringReverser()

    test_cases = [
        "hello",
        "Python programming is fun!",
        "",
        "A"
    ]

    for word in test_cases:
        reversed_word = reverser.reverse(word)
        print(f"Original: {word}")
        print(f"Reversed: {reversed_word}\n")