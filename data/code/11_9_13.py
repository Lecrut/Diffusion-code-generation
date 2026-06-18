import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_side_ratio(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides of a right triangle.
        
        The result is simplified by dividing both sides by their Greatest Common Divisor (GCD).
        
        Args:
            side_a (int): Length of the first side.
            side_b (int): Length of the second side.
            
        Returns:
            float: The ratio a/b in decimal form, where the fraction is simplified.
        """
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Side lengths must be positive integers.")

        common_divisor = math.gcd(side_a, side_b)
        
        # Simplify by dividing both sides by their GCD to get the simplest form of the ratio
        simplified_numerator = side_a // common_divisor
        simplified_denominator = side_b // common_divisor
        
        return float(simplified_numerator / simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    calc = GeometryCalculator()

    # Sample 1: Ratio of sides 6 and 8 (simplifies to 3/4 or 0.75)
    ratio_1 = calc.calculate_side_ratio(6, 8)
    
    # Sample 2: Ratio of sides 9 and 12 (simplifies to 3/4 or 0.75)
    ratio_2 = calc.calculate_side_ratio(9, 12)

    # Sample 3: Ratio of sides 5 and 13 (already simplified as they are coprime) -> approx 0.3846...
    ratio_3 = calc.calculate_side_ratio(5, 13)

    print(f"Ratio for sides 6 and 8: {ratio_1}")
    print(f"Ratio for sides 9 and 12: {ratio_2}")
    print(f"Ratio for sides 5 and 13: {ratio_3}")