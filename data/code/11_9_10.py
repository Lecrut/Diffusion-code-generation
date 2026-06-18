import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_side_ratio(self, side_a: float, side_b: float) -> str:
        """
        Calculates the ratio of two sides of a right triangle and returns it as an irreducible fraction.

        Args:
            side_a (float): Length of the first side.
            side_b (float): Length of the second side.

        Returns:
            str: A string representing the simplified ratio in the form "numerator/denominator".
                 If one value is zero, it returns a corresponding representation like "/1" or "0/1".
        """
        # Handle division by zero cases gracefully for clarity
        if side_b == 0:
            return f"{int(side_a)}/1"
        
        numerator = int(round(abs(side_a)))
        denominator = int(round(abs(side_b)))

        # If either input was not a clean integer representation due to float precision, round it first.
        # However, the problem implies exact side lengths often used in such calculations.

if __name__ == '__main__':
    pass
