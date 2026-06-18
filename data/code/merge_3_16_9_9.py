"""Utility module containing logic to determine positivity."""

class PositivityChecker:
    """A utility class for checking if a value is positive."""

    @staticmethod
    def is_positive(value):
        """
        Determine if the given numeric value is strictly greater than zero.

        Args:
            value (int | float): The number to check.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    # Hard-coded sample values for testing the static method.
    test_cases = [
        -5,   # Negative number
        0,    # Zero (not positive)
        3.14, # Positive float
        100,  # Large positive integer
    ]

    print("Testing PositivityChecker.is_positive():")
    for num in test_cases:
        result = PositivityChecker.is_positive(num)
        status = "Positive" if result else "Not Positive"
        print(f"{num} is {status}")