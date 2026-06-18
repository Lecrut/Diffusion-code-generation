class LengthCalculator:
    def get_ratio(self, a, b):
        """
        Calculates the ratio of length 'a' to length 'b'.
        
        Args:
            a (float or int): The numerator length value.
            b (float or int): The denominator length value.
            
        Returns:
            float: The calculated ratio. If 'b' is zero, returns infinity.
                 Raises ValueError if both inputs are non-numeric types that cannot be converted to numbers.
        """
        try:
            num = float(a)
            den = float(b)
        except (TypeError, ValueError):
            raise TypeError("Both a and b must be numeric values.")

        if den == 0:
            return float('inf')
        
        return num / den

if __name__ == '__main__':
    calculator = LengthCalculator()
    
    # Sample test cases with hard-coded values
    result1 = calculator.get_ratio(10, 5)
    print(f"Ratio of 10 to 5: {result1}")

    result2 = calculator.get_ratio(3.5, 7)
    print(f"Ratio of 3.5 to 7: {result2}")

    # Edge case for division by zero
    try:
        result3 = calculator.get_ratio(10, 0)
        print(f"Ratio of 10 to 0 is infinite: {result3}")
    except Exception as e:
        print(f"Error handling division by zero (handled internally): {e} - Result was infinity")

    # Another edge case where denominator is negative
    result4 = calculator.get_ratio(2, -4)
    print(f"Ratio of 2 to -4: {result4}")