class NumberChecker:
    """A class to check properties of numbers."""

    def check_positivity(self, value):
        """
        Determines if the provided numeric value is positive.

        Args:
            value (int or float): The number to evaluate.

        Returns:
            bool: True if value > 0, False otherwise.
        """
        return value > 0

if __name__ == '__main__':
    checker = NumberChecker()
    
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [5, -3, 0.1, 0, float('inf'), float('-inf')]

    print("Testing check_positivity method:")
    for val in test_values:
        result = checker.check_positivity(val)
        status = "Positive" if result else "Non-positive (zero or negative)"
        print(f"{val}: {status}")