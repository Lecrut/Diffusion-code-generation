class ValueChecker:
    """A class that provides utility methods to check properties of values."""

    def check_if_zero(self, value):
        """
        Determines if the input value is zero.

        This method checks both integer and floating-point zeros.
        It returns True if the absolute value of the number is less than a small epsilon
        (to handle floating-point inaccuracies), otherwise False.

        Args:
            value (int or float): The numeric value to check.

        Returns:
            bool: True if the value is effectively zero, False otherwise.
        """
        # Using a small epsilon for float comparison to avoid precision issues
        return abs(value) < 1e-9

if __name__ == '__main__':
    checker = ValueChecker()

    sample_values = [0, -0, 0.0, 1, -5, 3.14, 2e-10]

    for val in sample_values:
        result = checker.check_if_zero(val)
        print(f"Value {val} is zero? {result}")