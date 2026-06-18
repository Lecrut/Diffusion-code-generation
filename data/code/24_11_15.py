class NumberChecker:
    def check_negativity(self, value):
        """
        Determines if a given numeric input is negative.

        Args:
            value (int or float): The number to evaluate.

        Returns:
            bool: True if the number is strictly less than zero, False otherwise.
        """
        return isinstance(value, (int, float)) and value < 0

if __name__ == '__main__':
    checker = NumberChecker()

    # Sample test values with expected results
    sample_cases = [
        (-5,),          # Expected: True
        (0,),           # Expected: False
        (-3.14),        # Expected: True
        (27,),          # Expected: False
        -99,            # Expected: True
        0.0,            # Expected: False
    ]

    for value in sample_cases:
        result = checker.check_negativity(value)
        print(f"Value {value} is negative: {result}")