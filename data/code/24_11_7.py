class NumberChecker:
    """A class to check properties of numbers."""

    def check_negativity(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (int or float): The number to check.

        Returns:
            bool: True if the value is strictly less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_values = [-5, -3.14, 0, 2, 100]

    checker = NumberChecker()

    print("Testing NumberChecker.check_negativity():")
    for val in test_values:
        result = checker.check_negativity(val)
        status = "Negative" if result else "Non-negative (zero or positive)"
        print(f"{val}: {status}")