class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, word):
        """
        Reverses the input string in-place or returns a new reversed string.
        
        This method adheres to object-oriented best practices by encapsulating 
        behavior within an instance and returning a clean result without side effects 
        on the original argument (as strings are immutable).

        Args:
            word (str): The string to be reversed.

        Returns:
            str: A new string with characters in reverse order.
        
        Examples:
            >>> reverser = StringReverser()
            >>> reverser.reverse("hello")
            'olleh'
        """
        return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [
        "Python",
        "Hello, World!",
        "",
        "a"
    ]

    reverser = StringReverser()

    for word in test_cases:
        reversed_word = reverser.reverse(word)
        print(f'Original: "{word}" -> Reversed: "{reversed_word}"')