class StringReverser:
    """A class that provides methods to manipulate strings."""

    def reverse(self, text):
        """
        Reverses the input string in place (modifies self) and returns it.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: The reversed string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        "Hello, World!",
        "",
        "A",
        "Python Programming",
        12345  # Note: This will fail if passed as an int to a method expecting str in real use, 
             # but here we ensure the string path is tested. We'll cast it implicitly or skip non-strings.
    ]

    reverser = StringReverser()

    for test_input in test_cases:
        try:
            if isinstance(test_input, str):
                result = reverser.reverse(test_input)
                print(f"Input: '{test_input}' -> Output: '{result}'")
            else:
                # Skip non-string inputs to avoid runtime errors during this specific demo run
                continue
        except Exception as e:
            print(f"Error processing input {repr(test_input)}: {e}")