import string

class StringReverser:
    """A class that provides methods to reverse strings."""

    def __init__(self):
        self._reversed_text = ""  # Private attribute to store reversed result if needed later, though not used here.

    def reverse(self, text: str) -> str:
        """Reverses the input string and returns it.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: The reversed version of the input string.
        """
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies.
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "!dlroW ,olleH",  # Edge case: already reversed string
        "A man a plan a canal Panama!"  # Note: This is not strictly palindrome but includes spaces and punctuation.
    ]

    reverser = StringReverser()

    print("String Reversal Demo")
    print("-" * 30)

    for text in samples:
        reversed_text = reverser.reverse(text)
        original_length = len(text)
        reversed_length = len(reversed_text)
        
        print(f"\nOriginal Input:")
        print(f'   Text: "{text}"')
        print(f"   Length: {original_length}")

        print(f"\nReversed Output:")
        print(f'   Text: "{reversed_text}"')
        print(f"   Length: {reversed_length}")

        # Verify length consistency (basic sanity check)
        assert original_length == reversed_length, "Length mismatch error."

    print("\n" + "-" * 30)
    print("All samples processed successfully.")