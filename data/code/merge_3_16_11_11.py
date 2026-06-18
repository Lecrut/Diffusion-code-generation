class NumberChecker:
    """A class to check properties of numbers."""

    def check_positivity(self, value):
        """
        Determines if the provided numeric value is positive.

        Args:
            value (int or float): The number to evaluate.

        Returns:
            bool: True if the value is strictly greater than zero, False otherwise.
        
        Example:
            >>> checker = NumberChecker()
            >>> checker.check_positivity(5)
            True
            >>> checker.check_positivity(-3.0)
            False
            >>> checker.check_positivity(0)
            False
        """
        return value > 0

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    checker = NumberChecker()

    test_cases = [10, -5.7, 0, 3.14, float('inf'), float('-inf')]

    for value in test_cases:
        result = checker.check_positivity(value)
        print(f"Is {value} positive? {result}")