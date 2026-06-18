class LengthCalculator:
    """A utility class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """Calculates the ratio of length 'a' to length 'b'.
        
        Args:
            a (int or float): The numerator length.
            b (int or float): The denominator length.
            
        Returns:
            int or float: The result of dividing 'a' by 'b'.
            
        Raises:
            ZeroDivisionError: If the denominator 'b' is zero.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Arguments must be numeric.")
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero length.")

        return a / b

if __name__ == '__main__':
    # Sample execution without user input
    calculator = LengthCalculator()

    sample_a = 10.5
    sample_b = 2

    result_ratio = calculator.get_ratio(sample_a, sample_b)

    print(f"Ratio of {sample_a} to {sample_b}: {result_ratio}")