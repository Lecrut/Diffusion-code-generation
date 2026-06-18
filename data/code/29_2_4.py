class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, word):
        """
        Reverses the input string in-place (modifying self) and returns a new reversed string.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: A newly created string that is the reverse of 'word'.
        """
        return ''.join(reversed(word))

if __name__ == '__main__':
    # Create an instance of StringReverser
    reverser = StringReverser()

    # Hard-coded sample values to test functionality
    samples = [
        "hello",
        "Python programming is fun!",
        "",
        "A man, a plan, a canal: Panama"
    ]

    for word in samples:
        reversed_word = reverser.reverse(word)
        print(f"Original: {word}")
        print(f"Reversed:{reversed_word}\n")