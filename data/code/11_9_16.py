import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_side_ratio(self, side_a: float, side_b: float) -> tuple[float, int]:
        """
        Calculates the ratio of two sides of a right triangle and simplifies it.

        Args:
            side_a (float): Length of the first side.
            side_b (float): Length of the second side.

        Returns:
            tuple[float, int]: A tuple containing the simplified numerator 
                              as a float (side_a / gcd), denominator as an integer,
                              and the greatest common divisor used for simplification.
        """
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Side lengths must be positive numbers.")

        # Convert to integers to perform GCD calculation accurately
        a_int = int(round(side_a))
        b_int = int(round(side_b))

        gcd_val = math.gcd(a_int, b_int)

        simplified_numerator = side_a / gcd_val if isinstance(gcd_val, (int, float)) else round((a_int / gcd_val), 20)
        
        return simplified_numerator, b_int // gcd_val

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    calc = GeometryCalculator()

    # Sample case: sides of a right triangle (3, 4) -> ratio should simplify based on GCD(3,4)=1
    result_1_num, result_1_denom = calc.calculate_side_ratio(3, 4)
    
    # Another sample where simplification is more obvious if inputs were scaled multiples.
    # Let's use sides that are effectively integers for demonstration of the logic flow.
    side_a_sample = 6.0
    side_b_sample = 8.0
    
    ratio_num, ratio_denom = calc.calculate_side_ratio(side_a_sample, side_b_sample)

    print(f"Input Sides: {side_a_sample}, {side_b_sample}")
    print(f"Simplified Ratio Numerator (float): {ratio_num}")
    print(f"Simplified Ratio Denominator (int): {ratio_denom}")