class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.

        Args:
            a (int or float): The numerator length.
            b (int or float): The denominator length. Must not be zero.

        Returns:
            float: The ratio of a to b.

        Raises:
            ZeroDivisionError: If 'b' is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot calculate ratio with a zero divisor.")
        
        return a / b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    calc = LengthCalculator()

    try:
        result1 = calc.get_ratio(10, 5)
        print(f"Ratio of {10} to {5}: {result1}")

        result2 = calc.get_ratio(3.5, 7)
        print(f"Ratio of {3.5} to {7}: {result2:.4f}")

    except ZeroDivisionError as e:
        # Demonstrate error handling for invalid input (though not triggered by current samples).
        print(f"An error occurred: {e}")