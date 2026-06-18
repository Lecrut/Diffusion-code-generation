class StringReverser:
    """A class to reverse strings."""

    def reverse(self, word: str) -> str:
        """Returns the reversed version of the input string.
        
        Args:
            word (str): The string to be reversed.
            
        Returns:
            str: A new string with characters in reverse order.
        """
        return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "a"
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for word in test_cases:
        reversed_word = reverser.reverse(word)
        # Handle quotes around empty strings if original had any, though slicing handles it correctly. 
        # We just display the result directly as per requirement to avoid extra formatting issues with invisible chars like \n\n at end of string
        print(f"Original: '{word}' -> Reversed: '{reversed_word}'")