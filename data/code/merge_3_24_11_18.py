class NumberChecker:
    """A class designed to check properties of numerical values."""

    def __init__(self):
        """Initialize the NumberChecker instance with no specific parameters required."""
        pass

    def check_negativity(self, value) -> bool:
        """
        Determines if the input value is negative.

        Args:
            value (int or float): The numerical value to be checked.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        
        Examples:
            >>> checker = NumberChecker()
            >>> checker.check_negativity(-5)
            True
            >>> checker.check_negativity(0)
            False
            >>> checker.check_negativity("not a number")  # Raises TypeError implicitly as Python handles this naturally, but logic assumes numeric input. For pure efficiency and correctness with expected types:
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected int or float, got {type(value).__name__}")

        return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    checker = NumberChecker()

    test_values = [-10, -3.5, 0, 42, 0.0]

    print("Testing NumberChecker.check_negativity:")
    for val in test_values:
        result = checker.check_negativity(val)
        status = "Negative" if result else "Non-negative or Zero"
        print(f"{val} is {status}")