class LengthCalculator:
    """A class to perform calculations related to lengths."""

    def get_ratio(self, a: float, b: float) -> float:
        """Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (float): The first length value.
            b (float): The second length value. Must not be zero.

        Returns:
            float: The calculated ratio (a / b).

        Raises:
            ValueError: If 'b' is zero, to prevent division by zero error.
        """
        if b == 0:
            raise ValueError("Division by zero is undefined.")
        
        return a / b

if __name__ == '__main__':
    # Hard-coded sample values for testing the LengthCalculator class
    calculator = LengthCalculator()

    # Sample test case 1: Normal ratio calculation
    result_1 = calculator.get_ratio(10, 5)
    print(f"Ratio of {result_1}")  # Expected output: 2.0

    # Sample test case 2: Integer inputs resulting in float
    result_2 = calculator.get_ratio(7, 3)
    print(f"Ratio of {result_2}")  # Expected output: 2.333...

    # Sample test case 3: Negative values (handled correctly by division)
    result_3 = calculator.get_ratio(-10, -5)
    print(f"Ratio of {result_3}")  # Expected output: 2.0