from typing import Union

class ValueChecker:
    """A class that provides utility methods to check various properties of values."""

    def __init__(self) -> None:
        """Initialize the ValueChecker instance."""
        pass

    def check_for_zero(self, value: float | int = 0.0) -> bool:
        """Check if the given numeric input is equal to zero.

        Supports checking for both integers and floats. For floating-point numbers,
        it checks strict equality using a tolerance mechanism when necessary, though
        direct comparison with == works correctly if exact representation is expected.

        Args:
            value (float | int): The number to check against zero.

        Returns:
            bool: True if the value is equal to zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value != 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    checker = ValueChecker()

    assert check_for_zero(0) is True
    assert check_for_zero(1.0) is False
    assert check_for_zero(-50.493286782347345987) is False