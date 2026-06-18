class NumberChecker:
    """A utility class for checking numerical properties."""

    def check_negativity(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (int | float | str): The number to evaluate. If a string, it will be converted.

        Returns:
            bool: True if the value represents a negative number, False otherwise.
        """
        # Handle string inputs by converting to numeric type first
        try:
            num = float(value)
        except (ValueError, TypeError):
            return False
        
        return num < 0

if __name__ == '__main__':
    checker = NumberChecker()

    test_values = [
        -5,           # Negative integer -> True
        -3.14,        # Negative float -> True
        0,             # Zero -> False (zero is not negative)
        "hello",       # Non-numeric string -> False
        "",            # Empty string -> False
        "+7",          # Positive signed string -> False
        "-7",          # Negative signed string -> True
    ]

    for val in test_values:
        result = checker.check_negativity(val)
        print(f"Value '{val}' is negative: {result}")