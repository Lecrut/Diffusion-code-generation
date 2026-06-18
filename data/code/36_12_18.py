class StringReverser:
    """A class to reverse strings."""

    def reverse(self, text: str) -> str:
        """Returns a new string with characters in reversed order.
        
        Args:
            text (str): The input string to be reversed.
            
        Returns:
            str: A new string containing the characters of 'text' in reverse order.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_cases = [
        "Hello, World!",
        "",
        "A",
        "Python Programming"
    ]

    reverser = StringReverser()

    for text in test_cases:
        reversed_text = reverser.reverse(text)
        print(f"Original: '{text}'")
        print(f"Reversed: '{reversed_text}'")
        print("-" * 20)