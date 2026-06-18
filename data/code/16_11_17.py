class NumberChecker:
    """A class to check properties of numbers."""

    def check_positivity(self, value):
        """
        Determines if the provided numeric value is positive.

        A number is considered positive if it is strictly greater than zero.
        Non-numeric types will raise a TypeError.

        Args:
            value (int | float): The numerical value to evaluate.

        Returns:
            bool: True if value > 0, False otherwise.

        Raises:
            TypeError: If the input is not an int or float.
        """
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return value > 0
        
        raise TypeError(f"Expected a number, got {type(value).__name__}")

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input
    test_values = [10.5, -3, 0, True, False]

    print("Testing positivity checks:")
    for val in test_values:
        try:
            result = checker.check_positivity(val)
            status = "Positive" if result else "Not Positive (or Zero)"
            print(f"{val} -> {status}")
        except TypeError as e:
            print(f"{type(val).__name__} ({val}) raised an error: {e}")