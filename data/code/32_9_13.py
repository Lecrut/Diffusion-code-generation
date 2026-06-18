"""Utility module containing a static method to calculate string length."""

class LengthCalculator:
    """A utility class providing methods for calculating string lengths."""

    @staticmethod
    def calculate_length(text: str) -> int:
        """Calculate the number of characters in the given text.

        Args:
            text (str): The input string to measure.

        Returns:
            int: The length of the string.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = [
        "Hello, World!",
        "",
        "Python 3.x",
        "12345" * 100,
    ]

    calculator = LengthCalculator()

    print("Length Calculation Results:")
    for sample in samples:
        length = calculator.calculate_length(sample)
        print(f"'{sample[:10]}{'...' if len(sample) > 10 else ''}' -> {length} characters")