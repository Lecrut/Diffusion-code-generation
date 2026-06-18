class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (float or int): The numerator length.
            b (float or int): The denominator length. Must not be zero.

        Returns:
            float: The calculated ratio.

        Raises:
            ZeroDivisionError: If the denominator 'b' is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        
        return a / b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    calc = LengthCalculator()

    try:
        ratio1 = calc.get_ratio(10, 5)
        print(f"Ratio of {10} to {5}: {ratio1}")

        ratio2 = calc.get_ratio(-4, 8)
        print(f"Ratio of {-4} to {8}: {ratio2}")

        # Testing error handling for zero denominator
        try:
            ratio3 = calc.get_ratio(100, 0)
        except ZeroDivisionError as e:
            print(f"Caught expected error for division by zero: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")