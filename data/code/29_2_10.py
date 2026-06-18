class StringReverser:
    """A class to reverse strings."""

    def __init__(self):
        """Initialize the StringReverser instance with no arguments required."""
        pass

    @staticmethod
    def reverse(word) -> str:
        """Reverse the input string.
        
        Args:
            word (str): The string to be reversed.
            
        Returns:
            str: The reversed string.
        """
        return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or file I/O
    test_cases = ["hello", "Python Programming", "", "a"]

    reverser = StringReverser()

    for word in test_cases:
        reversed_word = reverser.reverse(word)
        print(f"Original: '{word}' -> Reversed: '{reversed_word}'")