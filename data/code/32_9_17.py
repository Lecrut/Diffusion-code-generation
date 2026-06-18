"""Utility module containing a static method to calculate string length."""

class StringUtilities:
    """A utility class providing helper methods for basic string operations."""

    @staticmethod
    def get_length(s: str) -> int:
        """Calculate the number of characters in the given string.

        Args:
            s (str): The input string to measure.

        Returns:
            int: The length of the string as an integer count of characters.
        """
        return len(s)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction.
    samples = [
        "Hello, World!",
        "",
        "Python 3.x",
        "a" * 100,
    ]

    print("String Length Calculation Results:")
    print("-" * 40)

    for sample in samples:
        length_value = StringUtilities.get_length(sample)
        display_str = repr(sample)[:50] + ("..." if len(repr(sample)) > 50 else "")
        print(f'String: {display_str!r} -> Length: {length_value}')