import math

class GeometryCalculator:
    """A class designed for basic geometry calculations involving right triangles."""

    def calculate_ratio(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides of a right triangle.
        
        The result is simplified by dividing both numerator and denominator 
        by their Greatest Common Divisor (GCD). If GCD is 1, the fraction remains as is.
        Returns the reduced decimal representation or the exact integer if applicable.

        Args:
            side_a (int): Length of the first side.
            side_b (int): Length of the second side.

        Returns:
            float: The simplified ratio a/b converted to float, 
                  or int if it is an exact whole number representation after simplification logic check.
        """
        # Ensure we are dealing with positive integers as per geometric context usually implying lengths > 0
        if not isinstance(side_a, (int, float)) or side_a <= 0:
            raise ValueError("side_a must be a positive integer.")
        
        if not isinstance(side_b, (int, float)) or side_b <= 0:
            raise ValueError("side_b must be a positive integer.")

        # Convert to integers for GCD calculation logic consistency with the prompt's "simplified using GCD" requirement.
        num = int(round(float(side_a)))
        den = int(round(float(side_b)))

        if side_a != num or side_b != den:
            raise ValueError("Inputs must be valid positive numbers suitable for integer ratio simplification.")

        # Calculate the Greatest Common Divisor (GCD) of numerator and denominator.
        common_divisor = math.gcd(num, den)

        simplified_numerator = num // common_divisor
        simplified_denominator = den // common_divisor

        return float(simplified_numerator / simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    calc = GeometryCalculator()

    # Test Case 1: Standard ratio (3/4) -> GCD is 1, no change essentially in value but shows logic path.
    result_1 = calc.calculate_ratio(3, 4)
    print(f"Ratio of sides 3 and 4: {result_1}")

    # Test Case 2: Ratio with common factor (6/8 -> simplifies to 3/4).
    result_2 = calc.calculate_ratio(6, 8)
    print(f"Simplified ratio of sides 6 and 8: {result_2}")

    # Test Case 10: Another example where GCD > 1 (9/15 -> simplifies to 3/5).
    result_3 = calc.calculate_ratio(9, 15)
    print(f"Simplified ratio of sides 9 and 15: {result_3}")

    # Test Case with same side lengths.
    result_4 = calc.calculate_ratio(7, 7)
    print(f"Ratio of equal sides (simplifies to 1): {result_4}")