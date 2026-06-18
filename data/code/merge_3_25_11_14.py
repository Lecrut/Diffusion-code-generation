"""Module to check if a value is zero."""

class ValueChecker:
    """A class that provides methods to verify specific properties of values."""

    def check_for_zero(self, value) -> bool:
        """Determines if the input 'value' is equal to zero.

        Args:
            value (int | float): The numerical value to be checked.

        Returns:
            bool: True if the value is exactly 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [0, -5, 3.14, 0.0, "zero", None]

    print("Testing check_for_zero method:")
    for val in test_values:
        result = checker.check_for_zero(val)
        status = "Zero" if result else "Not Zero"
        # Note: Non-numeric types will raise an error when compared to 0, 
        # which is expected Python behavior. We catch it here only to demonstrate logic flow 
        # but the core method relies on standard type comparison rules as per best practices.
        try:
            print(f"{val!r} -> {status}")
        except TypeError:
            print(f"{val!r} -> Type Error (Expected behavior for non-numeric types)")