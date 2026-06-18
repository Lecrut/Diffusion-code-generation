class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (float or int): The numerator length.
            b (float or int): The denominator length. Must not be zero.

        Returns:
            float: The result of dividing a by b.

        Raises:
            ZeroDivisionError: If the denominator 'b' is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        return a / b

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    calc = LengthCalculator()

    sample_a = 10.5
    sample_b = 2

    ratio_result = calc.get_ratio(sample_a, sample_b)
    print(f"Ratio of {sample_a} to {sample_b}: {ratio_result}")