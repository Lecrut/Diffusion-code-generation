class LengthCalculator:
    """A class to calculate ratios between two lengths."""

    def get_ratio(self, a, b):
        """Calculates the ratio of length 'a' to length 'b'.
        
        Args:
            a (int or float): The numerator length.
            b (int or float): The denominator length.
            
        Returns:
            float: The ratio of a to b.
            
        Raises:
            ZeroDivisionError: If the denominator is zero.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numeric.")
        
        return a / b

if __name__ == '__main__':
    calculator = LengthCalculator()
    
    # Sample values: length of side A is 10 units, length of side B is 5 units.
    sample_a = 10
    sample_b = 5
    
    ratio_value = calculator.get_ratio(sample_a, sample_b)
    print(f"The ratio of {sample_a} to {sample_b} is: {ratio_value}")