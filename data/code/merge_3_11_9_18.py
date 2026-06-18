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
            float: The ratio of side_a to side_b in its simplest form, represented as a decimal.
                   If either side is zero or negative, returns None.
        """
        if side_a <= 0 or side_b <= 0:
            return None

        # Calculate the GCD of the two sides
        common_divisor = math.gcd(side_a, side_b)

        # Simplify by dividing both sides by the GCD
        simplified_side_a = side_a // common_divisor
        simplified_side_b = side_b // common_divisor

        return simplified_side_a / simplified_side_b

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or command-line arguments.
    calculator = GeometryCalculator()

    # Sample 1: Classic Pythagorean triple (3, 4) -> ratio should be 0.75
    result_1 = calculator.calculate_side_ratio(3, 4)
    
    # Sample 2: Another triple (6, 8) which simplifies to the same as above
    result_2 = calculator.calculate_side_ratio(6, 8)

    # Sample 3: Non-triple numbers that share a common factor greater than 1 (e.g., 9 and 15 -> GCD is 3)
    result_3 = calculator.calculate_side_ratio(9, 15)

    print(f"Ratio of sides {3} and {4}: {result_1}")
    print(f"Ratio of sides {6} and {8}: {result_2}")
    print(f"Ratio of sides {9} and {15}: {result_3}")