import math

class TriangleCalculator:
    """A class designed for geometry calculations focusing on right triangles."""

    def calculate_ratio_simplified(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides of a right triangle and returns it simplified.

        The ratio is represented as a fraction (numerator / denominator).
        Both numerator and denominator are positive integers with no common factors other than 1.

        Args:
            side_a (int): First side length, must be greater than or equal to 0.
            side_b (int): Second side length, must be greater than or equal to 0.

        Returns:
            float: The simplified ratio as a decimal value.
        """
        if side_a < 0 or side_b < 0:
            raise ValueError("Side lengths must be non-negative.")

        # If either side is zero, the triangle degenerates; define behavior based on standard math limit intuition 
        # where division by zero raises an error in float context but logically one ratio is infinite.
        if side_a == 0 and side_b > 0:
            return float('inf')
        elif side_b == 0 and side_a > 0:
            return 0.0
        
        numerator = max(side_a, side_b)
        denominator = min(side_a, side_b)

        # Calculate GCD to simplify the fraction
        common_divisor = math.gcd(numerator, denominator)
        
        simplified_numerator = numerator // common_divisor
        simplified_denominator = denominator // common_divisor
        
        return simplified_numerator / simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    calc = TriangleCalculator()

    # Sample 1: Standard integer sides (3, 4) -> ratio should be 4/3 or 3/4 simplified to same representation logic
    result_1 = calc.calculate_ratio_simplified(3, 4)
    print(f"Ratio of side 3 and side 4 is: {result_1}")

    # Sample 2: Larger sides (60, 85 - from a Pythagorean triple scaled by 1/19 or similar logic where GCD helps) 
    # Actually let's use standard triples for clarity. e.g., 5-12-13 triangle.
    result_2 = calc.calculate_ratio_simplified(5, 12)
    print(f"Ratio of side 5 and side 12 is: {result_2}")

    # Sample 3: Equal sides (isosceles right triangle effectively treated here as a ratio test regardless of hypotenuse context for this task's scope on 'two sides')
    result_3 = calc.calculate_ratio_simplified(7, 7)
    print(f"Ratio of side 7 and side 7 is: {result_3}")

    # Sample with zero to demonstrate edge case handling in float output (though not a valid right triangle side strictly >0 for area)
    try:
        result_zero = calc.calculate_ratio_simplified(5, 0)
        print(f"Ratio of side 5 and side 0 is: {result_zero}")
    except Exception as e:
        # The logic above handles zero denominator by returning float('inf') explicitly for the case where numerator > 0. 
        if result_zero == float('inf'):
            pass

    # Demonstrate non-integer simplification capability (e.g., 12 and 8 -> GCD is 4, ratio becomes 3/2)
    result_fractional = calc.calculate_ratio_simplified(12, 8)
    print(f"Ratio of side 12 and side 8 is: {result_fractional}") # Should be 1.5 (3/2)