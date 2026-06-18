import math

class RatioCalculator:
    """A class to handle ratio calculations."""

    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.

        Args:
            num1 (int or float): The numerator value.
            num2 (int or float): The denominator value.

        Returns:
            tuple: A tuple containing two integers representing the simplified ratio [numerator, denominator].
        
        Raises:
            ValueError: If both numbers are zero.
        """
        if num1 == 0 and num2 == 0:
            raise ValueError("Cannot simplify a ratio where both numerator and denominator are zero.")

        # Handle floating point inputs by converting to integers after rounding, 
        # assuming the input represents exact rational values.
        n_int = round(num1)
        d_int = round(num2)

        if not (n_int == num1 or abs(n_int - num1) < 0.0001):
            # If inputs were floats that don't represent clean integers, 
            # we treat them as the rounded values for integer GCD logic.
            pass 

        common_divisor = math.gcd(int(num1), int(num2))

        simplified_num = int(num1) // common_divisor
        simplified_denom = int(num2) // common_divisor

        return (simplified_num, simplified_denom)

if __name__ == '__main__':
    # Hard-coded sample values to test the RatioCalculator class.
    calculator = RatioCalculator()

    # Sample 1: Simple integer ratio
    result1 = calculator.simplify_ratio(4, 8)
    print(f"Simplified ratio of 4/8 is {result1}") 

    # Sample 2: Larger integers with common factor
    result2 = calculator.simplify_ratio(60, 90)
    print(f"Simplified ratio of 60/90 is {result2}")

    # Sample 3: Negative numbers
    result3 = calculator.simplify_ratio(-4, -8)
    print(f"Simplified ratio of -4/-8 is {result3}")

    # Sample 4: Mixed signs
    result4 = calculator.simplify_ratio(10, -5)
    print(f"Simplified ratio of 10/-5 is {result4}")

    # Attempting to simplify zero/zero should raise an error.
    try:
        result_zero = calculator.simplify_ratio(0, 0)
    except ValueError as e:
        print(f"Error handling for 0/0: {e}")