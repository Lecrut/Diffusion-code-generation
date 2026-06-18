class NumberChecker:
    """A class to check properties of numerical values."""

    def check_negativity(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [-5, -3.14, 0, 2, 10]

    print("Testing NumberChecker.check_negativity:")
    for val in test_values:
        result = checker.check_negativity(val)
        status = "Negative" if result else "Non-negative"
        print(f"{val} is {status}")