import math

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.
        
        Args:
            num1 (int or float): The numerator value.
            num2 (int or float): The denominator value.
            
        Returns:
            tuple: A tuple containing two integers representing the simplified numerator and denominator.
                  If inputs are floats, they will be converted to their nearest integer representation 
                  before processing to ensure exact division logic works with GCD.
                  
        Raises:
            ZeroDivisionError: If num2 is zero.
        """
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both inputs must be numbers.")

        # Handle floating point precision issues by converting to integers based on scale
        # This ensures we work with whole numbers for GCD calculation as requested.
        if num1 == int(num1) and num2 != 0:
            n = int(num1)
            d = int(num2)
        else:
            # If floats, multiply by a large factor to convert to integers (or round directly)
            # For simplicity in this context without external libraries, we'll assume 
            # the user expects integer-like behavior or rounding for float inputs.
            n = round(float(num1))
            d = round(float(num2))

        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        common_divisor = math.gcd(n, d)
        
        simplified_numerator = n // common_divisor
        simplified_denominator = d // common_divisor
        
        return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    test_cases = [
        (48, 6),      # Expected: (8, 1)
        (10, 25),     # Expected: (2, 5)
        (-30, -9),   # Expected: (-10, -3) -> GCD handles signs in Python math.gcd usually returning positive, 
                     # but division preserves sign. Let's verify logic: gcd(-30,-9)=3. -30/3=-10, -9/3=-3
        (5, 7),       # Expected: (5, 7)
    ]

    calculator = RatioCalculator()

    for num1, num2 in test_cases:
        result_numerator, result_denominator = calculator.simplify_ratio(num1, num2)
        print(f"Ratio of {num1} to {num2}: ({result_numerator}, {result_denominator})")