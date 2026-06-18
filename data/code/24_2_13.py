class NumberChecker:
    """A utility class to check properties of numbers."""

    def check_if_negative(self, value):
        """Determines if the input value is negative.

        Args:
            value (any numeric type or object supporting comparison with 0): The number to check.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    sample_values = [
        -5,
        10,
        0,
        -3.5,
        float('inf'),
        float('-inf')
    ]

    for value in sample_values:
        is_negative = checker.check_if_negative(value)
        print(f"{value} is negative: {is_negative}")