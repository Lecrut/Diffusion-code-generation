class ValueChecker:
    """A class to check if a given value is zero."""

    def check_if_zero(self, value):
        """
        Determines if the input value is exactly zero.

        Args:
            value (int or float): The number to be checked.

        Returns:
            bool: True if value is 0, False otherwise.
        """
        return value == 0

if __name__ == '__main__':
    checker = ValueChecker()

    # Hard-coded sample values running without user input or external dependencies
    test_cases = [0, -5, 3.14, float('inf'), "Zero"]

    for val in test_cases:
        try:
            result = checker.check_if_zero(val)
            print(f"Is {val} zero? {result}")
        except Exception as e:
            # Handle cases where value might not be numeric (e.g., string) gracefully
            if isinstance(val, str):
                print(f"{val}: Cannot numerically evaluate to zero.")
            else:
                raise e

    # Additional explicit test for clarity
    assert checker.check_if_zero(0) is True
    assert checker.check_if_zero(-1) is False
    assert checker.check_if_zero(2.5) is False