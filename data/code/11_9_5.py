import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def get_side_ratio(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides (side_a to side_b) of a right triangle.
        
        The resulting fraction is simplified by dividing both sides by their Greatest Common Divisor (GCD).
        Returns the decimal representation of this simplified ratio.
        
        Args:
            side_a (int): Length of the first side.
            side_b (int): Length of the second side.
            
        Returns:
            float: The simplified ratio as a floating-point number.
             
        Raises:
            ValueError: If either side length is less than or equal to zero.
        """
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Side lengths must be greater than zero.")

        # Calculate the Greatest Common Divisor of both sides for simplification
        common_divisor = math.gcd(side_a, side_b)

        simplified_numerator = side_a // common_divisor
        simplified_denominator = side_b // common_divisor
        
        return simplified_numerator / simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input.
    calc = GeometryCalculator()

    # Sample 1: Ratio of sides 6 and 8 simplifies to 3/4 (0.75)
    result_1 = calc.get_side_ratio(6, 8)
    
    # Sample 2: Ratio of sides 9 and 12 simplifies to 3/4 (0.75)
    result_2 = calc.get_side_ratio(9, 12)

    # Sample 3: Ratio of the hypotenuse (13) and a leg (12) from a 5-12-13 triangle simplifies to 13/12 (~1.0833)
    result_3 = calc.get_side_ratio(13, 12)

    print(f"Ratio of sides 6 and 8: {result_1}")       # Expected: 0.75
    print(f"Ratio of sides 9 and 12: {result_2}")   # Expected: 0.75
    print(f"Ratio of sides 13 and 12: {result_3}") # Expected: ~1.0833