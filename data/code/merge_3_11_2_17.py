import math

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.
        
        Parameters:
            num1 (int or float): The numerator value.
            num2 (int or float): The denominator value.
            
        Returns:
            tuple: A tuple containing two integers representing the simplified ratio [numerator, denominator].
                   If input types are not int/float convertible to int and result is 0/denom handled as integer logic.
        
        Raises:
            ZeroDivisionError: If num2 is zero.
        """
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Both inputs must be numeric.")

        # Handle non-integer inputs by converting to integers after rounding for practical ratio logic
        try:
            n = int(round(num1))
            d = int(round(num2))
        except Exception:
            raise ValueError("Inputs must represent valid numbers convertible to integers.")

        if d == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # Determine sign for consistency (ensure positive denominator)
        common_divisor = math.gcd(n, d)
        
        simplified_numerator = n // common_divisor
        simplified_denominator = d // common_divisor
        
        if simplified_denominator < 0:
            simplified_numerator = -simplified_numerator
            simplified_denominator = -simplified_denominator
            
        return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    calculator = RatioCalculator()