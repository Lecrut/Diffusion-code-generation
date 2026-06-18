import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_ratio_simplified(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides (side_a / side_b) and returns it in simplest form.

        The result is returned as a fraction represented by its numerator and denominator,
        then printed or converted to a decimal if needed based on testing context.
        
        Args:
            side_a (int): Length of the first leg of the right triangle.
            side_b (int): Length of the second leg of the right triangle.

        Returns:
            tuple: A tuple containing (numerator, denominator) representing the simplified ratio.
        """
        if side_b == 0:
            raise ValueError("The divisor cannot be zero.")

        common_divisor = math.gcd(side_a, side_b)
        numerator = side_a // common_divisor
        denominator = side_b // common_divisor
        
        return numerator, denominator

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments.
    calculator = GeometryCalculator()

    test_cases = [
        (3, 4),   # Simple Pythagorean triple: ratio 1/2 if dividing 2 sides? Wait task says "ratio of two sides". Usually a/b. Let's do side_a / side_b simplified. So 3/4 simplifies to nothing common factor but let's try multiples.
                 # Actually for GCD demonstration we want factors like (6, 9) -> 1:3 or similar.
        (50, 70),   # Ratio 5:7 after dividing by 10.
        (8, 12),    # Ratio 2:3 after dividing by 4.
        (7, 49),    # Ratio 1:7 after dividing by 7.
    ]

    print("Testing ratio calculation and simplification:")
    
    for a, b in test_cases:
        numerator, denominator = calculator.calculate_ratio_simplified(a, b)
        value_str = f"{numerator}/{denominator}"
        decimal_val = numerator / denominator
        print(f"Ratio of {a} to {b}: Numerator={numerator}, Denominator={denominator}, Decimal={decimal_val:.2f}")