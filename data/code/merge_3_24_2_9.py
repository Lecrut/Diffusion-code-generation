class NumberChecker:
    """A class to check properties of numbers."""

    def check_if_negative(self, value):
        """
        Determines if the input value is negative.

        Args:
            value (int or float): The number to check.

        Returns:
            bool: True if the value is less than zero, False otherwise.
        """
        return value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [
        -5,      # Negative integer
        0,       # Zero (not negative)
        3.14,    # Positive float
        -2.718,  # Negative float
        None     # Edge case: should raise an error or handle gracefully depending on design; here we assume valid numeric input per task scope but let it fail naturally for robustness if non-numeric is passed unless specified otherwise. Since the task implies checking 'if negative', we expect numbers. We will pass a mix of types to demonstrate behavior.)
    ]

    # Adjusting test_values slightly to ensure all are comparable and relevant to the logic, 
    # excluding None as it's not strictly numeric for this specific check without type handling instructions.
    valid_test_values = [-5, 0, 3.14, -2.718]

    print("Testing NumberChecker.check_if_negative:")
    for val in valid_test_values:
        result = checker.check_if_negative(val)
        status = "Negative" if result else "Non-negative"
        print(f"{val} is {status}")