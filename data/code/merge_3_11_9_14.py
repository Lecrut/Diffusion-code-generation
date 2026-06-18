import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_side_ratio(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides (side_a / side_b) of a triangle.
        
        The result is simplified by dividing both numerator and denominator 
        by their Greatest Common Divisor (GCD), then converted to a float for display.

        :param side_a: Length of the first side as an integer or float convertible to int.
        :param side_b: Length of the second side as an integer or float convertible to int.
        :return: The simplified ratio of side_a to side_b as a float.
        """
        # Ensure inputs are integers for GCD calculation, handling potential floats that represent whole numbers
        if isinstance(side_a, float) and not math.is_integer(side_a):
            raise ValueError("side_a must be an integer or a number effectively equal to one.")
        if isinstance(side_b, float) and not math.is_integer(side_b):
            raise ValueError("side_b must be an integer or a number effectively equal to one.")

        int_side_a = int(round(float(side_a)))
        int_side_b = int(round(float(side_b)))

        # Validate that we are not dividing by zero
        if int_side_b == 0:
            raise ZeroDivisionError("side_b cannot be zero.")

        # Calculate the GCD of the two sides to simplify the ratio fractionally before returning float representation.
        gcd_value = math.gcd(int_side_a, int_side_b)

        simplified_numerator = int_side_a // gcd_value
        simplified_denominator = int_side_b // gcd_value

        return simplified_numerator / simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    calc = GeometryCalculator()

    # Sample 1: Classic Pythagorean triple ratio (3, 4) -> should be 0.75
    result_1 = calc.calculate_side_ratio(3, 4)
    print(f"Ratio for sides 3 and 4: {result_1}")

    # Sample 2: Another simple case (6, 8) which simplifies to the same as above -> should be 0.75
    result_2 = calc.calculate_side_ratio(6, 8)
    print(f"Ratio for sides 6 and 8: {result_2}")

    # Sample 3: Non-trivial integers (10, 14) which simplifies to 5/7 -> approx 0.7142857
    result_3 = calc.calculate_side_ratio(10, 14)
    print(f"Ratio for sides 10 and 14: {result_3}")

    # Sample 4: Equal sides (ratio should be 1.0 regardless of value due to GCD normalization if integers are equal)
    result_4 = calc.calculate_side_ratio(5, 5)
    print(f"Ratio for sides 5 and 5: {result_4}")