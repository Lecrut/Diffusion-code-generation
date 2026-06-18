import math

class GeometryCalculator:
    """A class designed for geometry calculations."""

    def simplify(self, numerator, denominator):
        """Calculates the ratio of two sides as a simplified fraction.
        
        Args:
            numerator (int): The first side length (numerator).
            denominator (int): The second side length (denominator).
            
        Returns:
            tuple: A tuple containing the simplified numerator and denominator integers.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        common_divisor = math.gcd(abs(numerator), abs(denominator))

        return (numerator // common_divisor, denominator // common_divisor)

if __name__ == '__main__':
    # Hard-coded sample values representing two sides of a right triangle.
    side_a = 30528
    side_b = 19674
    
    calculator = GeometryCalculator()
    
    ratio_numerator, ratio_denominator = calculator.simplify(side_a, side_b)

    print(f"Original Ratio: {side_a}/{side_b}")
    print(f"Simplified Ratio: {ratio_numerator}/{ratio_denominator}")