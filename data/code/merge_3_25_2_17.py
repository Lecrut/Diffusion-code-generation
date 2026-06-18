class ValueChecker:
    """A class designed to check if a given value is zero."""

    def check_if_zero(self, value):
        """
        Determines if the input value is equal to zero.

        Args:
            value (int or float): The numeric value to be checked.

        Returns:
            bool: True if value is 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Hard-coded sample values for testing without user input
    test_values = [0, -1, 1, 3.14, 0.0]

    print("Testing ValueChecker.check_if_zero():")
    for val in test_values:
        result = checker.check_if_zero(val)
        status = "Is zero" if result else "Not zero"
        print(f"{val} ({type(val).__name__}): {status}")