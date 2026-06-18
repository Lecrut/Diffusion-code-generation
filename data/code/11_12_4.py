class LengthCalculator:
    """A utility class for calculating ratios between two lengths."""

    def get_ratio(self, a, b):
        """
        Calculate the ratio of length 'a' to length 'b'.

        Args:
            a (int or float): The numerator length.
            b (int or float): The denominator length.

        Returns:
            int or float: The result of dividing a by b, rounded to 
                         four decimal places for standard precision requirements.

        Raises:
            ZeroDivisionError: If the denominator 'b' is zero.
        """
        if isinstance(b, (int, float)) and not isinstance(a, (int, float)):
            raise TypeError("Both length arguments must be numeric types.")
        
        return round(a / b, 4)

if __name__ == '__main__':
    # Sample execution block with hard-coded values.
    calculator = LengthCalculator()

    sample_cases = [
        (10, 5),      # Expected: 2.0
        (7, 3),       # Non-integer result example
        (0, 4),       # Edge case check (though division is handled mathematically)
    ]

    for length_a, length_b in sample_cases:
        try:
            ratio = calculator.get_ratio(length_a, length_b)
            print(f"Ratio of {length_a} to {length_b}: {ratio}")
        except ZeroDivisionError as e:
            print(f"Error dividing by zero: {e}")