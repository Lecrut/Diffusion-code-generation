class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (float or int): The numerator length.
            b (float or int): The denominator length.

        Returns:
            float: The calculated ratio if successful; None otherwise.

        Raises:
            ValueError: If either input is not numeric, zero for 'b', 
                       or non-finite values are provided.
        """
        # Validate inputs to ensure they are numbers and handle edge cases efficiently
        try:
            num_a = float(a)
            num_b = float(b)

            if not (num_a.is_finite() and num_b.is_finite()):
                raise ValueError("Inputs must be finite numeric values.")

            # Check for division by zero to prevent runtime errors
            if num_b == 0:
                return None

            ratio = num_a / num_b
            return float(ratio)
        except (TypeError, ValueError):
            return None

if __name__ == '__main__':
    calculator = LengthCalculator()

    # Sample test cases with hard-coded values
    sample_cases = [
        ("Valid positive integers", 10, 5),      # Expected: 2.0
        ("Zero denominator (should handle gracefully)", 10, 0),   # Expected: None
        ("Negative lengths", -4, 8),             # Expected: -0.5
        ("Float inputs", 3.5, 7.0),              # Expected: 0.5
    ]

    for description, a_val, b_val in sample_cases:
        result = calculator.get_ratio(a_val, b_val)
        print(f"{description}: get_ratio({a_val}, {b_val}) = {result}")