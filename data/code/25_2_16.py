class ValueChecker:
    """A class that checks if a given value is zero."""

    def check_if_zero(self, value):
        """
        Determines if the input value is equal to zero.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if value is 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()
    
    # Hard-coded sample values for testing
    test_values = [0, -1, 1, 2.5, 0.0]

    print("Checking if the following values are zero:")
    for val in test_values:
        result = checker.check_if_zero(val)
        status = "Is Zero" if result else "Not Zero"
        print(f"{val} -> {status}")