"""Utility module containing a static method to calculate string length."""

class LengthCalculator:
    """A utility class providing methods for calculating text lengths."""

    @staticmethod
    def get_length(text: str) -> int:
        """Calculate the total character count in the provided string.

        Args:
            text (str): The input string to measure.

        Returns:
            int: The number of characters in the string.

        Raises:
            TypeError: If the input is not a string instance.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected 'str', got {type(text).__name__}")

        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello, World!",
        "",
        12345,
        None,
    ]

    for item in samples:
        try:
            result = LengthCalculator.get_length(item) if isinstance(item, str) else f"Input type {type(item).__name__}"
            print(f"Length of '{item}': {result}")
        except TypeError as e:
            print(f"Error calculating length for {repr(item)}: {e}")