class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """Calculates the ratio of length 'a' to length 'b'.
        
        Args:
            a (float or int): The numerator length.
            b (float or int): The denominator length. Must not be zero.
            
        Returns:
            float: The ratio of a to b.
            
        Raises:
            ZeroDivisionError: If 'b' is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        return a / b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    calculator = LengthCalculator()

    try:
        ratio1 = calculator.get_ratio(10, 5)
        print(f"Ratio of {10} to {5}: {ratio1}")

        ratio2 = calculator.get_ratio(-4, 8)
        print(f"Ratio of {-4} to {8}: {ratio2}")

    except ZeroDivisionError as e:
        # Demonstrating error handling for division by zero.
        try:
            bad_result = calculator.get_ratio(10, 0)
        except ZeroDivisionError:
            print(f"Caught expected error when dividing by zero: {e}")