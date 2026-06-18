class StringReverser:
    """A class that provides methods to reverse strings."""

    def reverse(self, text: str) -> str:
        """
        Reverses the input string and returns it as a new string.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new string which is the reverse of the input `text`.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_cases = [
        "hello",
        "Python programming",
        "",
        "A man a plan a canal Panama!",
    ]

    reverser = StringReverser()

    print("String Reversal Results:")
    for text in test_cases:
        reversed_text = reverser.reverse(text)
        if not text:  # Handle empty string case explicitly for clarity
            print(f'Input: "{text}" -> Output: (empty string)')
        else:
            print(f'Input: "{text}" -> Output: "{reversed_text}"')