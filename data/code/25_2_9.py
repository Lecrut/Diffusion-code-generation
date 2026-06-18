class ValueChecker:
    """A class that provides methods to check properties of numerical values."""

    def check_if_zero(self, value):
        """
        Determines if the input value is zero.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if the value is exactly zero, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [0, -1, 1, 0.0, 3.14]

    print("Testing check_if_zero method:")
    for val in test_values:
        result = checker.check_if_zero(val)
        status = "Is zero" if result else "Not zero"
        print(f"{val}: {status}")