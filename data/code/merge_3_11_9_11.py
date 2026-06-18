import math

class GeometryCalculator:
    """A class designed for geometry calculations."""

    @staticmethod
    def simplify_fraction(numerator, denominator):
        """
        Calculates the ratio of two sides and returns it as a simplified fraction (numerator, denominator).
        
        Args:
            numerator (int): The first side length.
            denominator (int): The second side length.
            
        Returns:
            tuple: A tuple containing the simplified numerator and denominator.
        """
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Both sides must be integers.")
        
        # Handle zero division case for simplicity (though geometrically side > 0 usually)
        if denominator == 0:
            return numerator, 1
            
        common_divisor = math.gcd(abs(numerator), abs(denominator))
        
        simplified_num = numerator // common_divisor
        simplified_denom = denominator // common_divisor
        
        # Ensure the sign is on the numerator for consistency (denominator always positive)
        if simplified_denom < 0:
            return -simplified_num, -1 * simplified_denom
            
        return simplified_num, simplified_denom

if __name__ == '__main__':
    calculator = GeometryCalculator()
    
    # Sample values representing the two sides of a right triangle (e.g., legs)
    side_a = 6
    side_b = 8
    
    ratio_numerator, ratio_denominator = calculator.simplify_fraction(side_a, side_b)
    
    print(f"Ratio of side {side_a} to side {side_b}:")
    print(f"Simplified fraction: {ratio_numerator}/{ratio_denominator}")