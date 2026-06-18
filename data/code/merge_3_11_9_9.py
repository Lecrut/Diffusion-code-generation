import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_side_ratio(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides (a and b) of a right triangle.
        The result is simplified by dividing both numbers by their Greatest Common Divisor (GCD).

        Args:
            side_a (int): Length of the first side.
            side_b (int): Length of the second side.

        Returns:
            float: The ratio a/b expressed as a decimal after simplification logic is applied to inputs.
                  Note: Simplifying the fraction for a float result involves calculating the reduced form,
                  then converting back to float which might not change the value visually unless precision differs greatly,
                  but strictly following "simplified using GCD" implies reducing the fraction if used as rational representation.
        """
        
        # Handle zero or negative inputs gracefully by taking absolute values for geometric context
        a = abs(side_a)
        b = abs(side_b)

        if a == 0 and b == 0:
            raise ValueError("Both sides cannot be zero.")
            
        if a < 0 or b < 0:
            # For length ratios, treat as absolute values. 
            # If the sign matters for direction/ordering in specific contexts, it could differ here.
            pass 

        # Calculate GCD to simplify the ratio fraction logic conceptually
        common_divisor = math.gcd(a, b)

        simplified_a = a // common_divisor
        simplified_b = b // common_divisor

        return float(simplified_a / simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    
    calc = GeometryCalculator()
    
    # Sample 1: Standard 3-4-5 triangle, ratio of legs (2 sides). GCD(3,4) is 1. Ratio 0.75
    result_1 = calc.calculate_side_ratio(3, 4)
    print(f"Ratio for sides 3 and 4: {result_1}")

    # Sample 2: Sides with a common factor (e.g., 6-8). GCD is 2. Reduced would be 3/4 -> 0.75.
    result_2 = calc.calculate_side_ratio(6, 8)
    print(f"Ratio for sides 6 and 8: {result_2}")

    # Sample 3: Pythagorean triple (9-12). GCD is 3. Reduced 3/4 -> 0.75.
    result_3 = calc.calculate_side_ratio(9, 12)
    print(f"Ratio for sides 9 and 12: {result_3}")

    # Sample 4: Non-integer related but integer inputs (e.g., 8 to 6). Ratio > 1. GCD is 2 -> 4/3.
    result_4 = calc.calculate_side_ratio(8, 6)
    print(f"Ratio for sides 8 and 6: {result_4}")

    # Sample 5: Powers of the same base (e.g., 10 to 5). GCD is 5 -> 2/1. Ratio 2.0.
    result_5 = calc.calculate_side_ratio(10, 5)
    print(f"Ratio for sides 10 and 5: {result_5}")