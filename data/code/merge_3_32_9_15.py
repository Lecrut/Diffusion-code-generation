"""Utility module containing a static method to calculate string length."""

class LengthCalculator:
    """A utility class providing methods for calculating text lengths."""

    @staticmethod
    def get_length(text: str) -> int:
        """Calculate the number of characters in the given string.

        Args:
            text (str): The input string to measure.

        Returns:
            int: The length of the string as a non-negative integer.
        """
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction.
    samples = [
        "Hello, World!",
        "",
        "Python is awesome.",
        "a" * 1000,
    ]

    calculator = LengthCalculator()

    print("String Length Calculation Results:")
    print("-" * 30)

    for sample in samples:
        length = calculator.get_length(sample)
        display_text = repr(sample)[:50] + "..." if len(repr(sample)) > 50 else repr(sample)
        print(f"'{display_text}' -> Length: {length}")