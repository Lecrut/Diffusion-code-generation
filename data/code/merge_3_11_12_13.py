class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (float or int): The numerator length.
            b (float or int): The denominator length.

        Returns:
            float: The calculated ratio as an integer if exact, otherwise rounded to 2 decimal places.

        Raises:
            ValueError: If 'b' is zero, which would cause division by error.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")

        result = a / b
        return round(result, 2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    calculator = LengthCalculator()

    test_cases = [
        (10, 5),      # Expected: 2.0
        (7, 3),       # Expected: 2.33
        (-4, 8),      # Expected: -0.5
        (0, 10),      # Expected: 0.0
    ]

    for length_a, length_b in test_cases:
        try:
            ratio = calculator.get_ratio(length_a, length_b)
            print(f"Ratio of {length_a} to {length_b}: {ratio}")
        except ValueError as e:
            print(f"Error calculating ratio for {length_a}, {length_b}: {e}")

    # Additional test case that should raise an error
    try:
        calculator.get_ratio(5, 0)
    except ValueError as e:
        print(f"Caught expected error: {e}")