"""Utility module for calculating string length with normalization."""

class StringUtils:
    """A utility class providing static methods for string operations."""

    @staticmethod
    def get_normalized_length(text: str) -> int:
        """
        Calculate the normalized length of a given text.

        Normalization involves converting the text to lowercase and stripping
        leading/trailing whitespace before counting characters.

        Args:
            text (str): The input string to measure.

        Returns:
            int: The normalized character count of the string.
        """
        return len(text.lower().strip())

if __name__ == '__main__':
    # Sample data without user interaction or external dependencies.
    sample_texts = [
        "  Hello, World! ",
        "\n\tPython is great\r\n",
        "",
        "   \t   ",
    ]

    for text in sample_texts:
        length = StringUtils.get_normalized_length(text)
        print(f"Normalized length of '{text}': {length}")