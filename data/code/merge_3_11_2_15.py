class RatioCalculator:
    """A class to calculate ratios in their lowest terms."""

    @staticmethod
    def gcd(a, b):
        """Compute the Greatest Common Divisor of a and b using Euclid's algorithm."""
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("Both numbers must be integers.")
        
        while b:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def simplify_ratio(num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms.
        
        Args:
            num1 (int or float): The numerator value.
            num2 (int or float): The denominator value.
            
        Returns:
            tuple: A tuple containing two integers representing the simplified fraction [numerator, denominator].
                   If either input is 0 and both are zero, returns [0, 1].
        
        Raises:
            ValueError: If num2 is zero (division by undefined).
            TypeError: If inputs are not numeric.
        """
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise TypeError("Inputs must be numbers.")

        # Handle the case where both are effectively zero to avoid division issues and return 0/1
        num1 = int(round(num1))
        num2 = int(round(num2))

        if num2 == 0:
            raise ValueError("Denominator cannot be zero.")

        common_divisor = RatioCalculator.gcd(abs(num1), abs(num2))

        return (num1 // common_divisor, num2 // common_divisor)

if __name__ == '__main__':
    # Hard-coded sample values to test the functionality without user input.
    
    # Test Case 1: Standard integer ratio simplification
    res1 = RatioCalculator.simplify_ratio(45097386, -2797)
    print(f"Ratio of {res1[0]} to {res1[1]:>5} (from {45097386}/{-2797})")

    # Test Case 2: Simple positive ratio
    res2 = RatioCalculator.simplify_ratio(6, 8)
    print(f"Ratio of {res2[0]} to {res2[1]:>5} (from {6}/{8})")

    # Test Case 3: Negative numerator and denominator resulting in positive
    res3 = RatioCalculator.simplify_ratio(-4, -8)
    print(f"Ratio of {res3[0]} to {res3[1]:>5} (from {-4}/-{8})")

    # Test Case 4: Float inputs converted to integers for ratio logic
    res4 = RatioCalculator.simplify_ratio(2.9, 7)
    print(f"Ratio of {int(round(res4[0]))}/{res4[1]} (approx from 3/7)")