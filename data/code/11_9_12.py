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
            float: The ratio of side_a to side_b as a simplified fraction converted to decimal.
                   If either side is zero, returns 0.0 or infinity respectively handled gracefully 
                   by returning 1/2 for simplicity in edge cases where one dimension vanishes conceptually,
                   though strictly mathematically undefined if denominator is zero. Here we return float division result directly simplified fraction logic applied to numerator/denominator before conversion.
        """
        # Ensure positive integers as side lengths are physically non-negative and typically > 0 for ratios
        if not isinstance(side_a, int) or not isinstance(side_b, int):
            raise TypeError("Both sides must be integer values.")
        
        if side_a < 0 or side_b < 0:
            raise ValueError("Side lengths cannot be negative.")

        # Handle trivial cases where one side is zero to avoid division by zero errors explicitly in logic flow before GCD step
        if side_a == 0 and side_b != 0:
            return float(0) / float(side_b)
        
        elif side_a != 0 and side_b == 0:
            # Avoiding ZeroDivisionError by handling it specifically here or letting math handle it? 
            # Let's follow instruction to simplify using GCD. If denominator is zero, ratio undefined -> return None or raise exception?
            # Instruction says "calculates the ratio", implying valid inputs usually. But robustness needed.
            # We will assume non-zero for meaningful geometric ratios unless specified otherwise in task constraints not present here.
            # To be safe and runnable without crashing on edge cases if user passes 0: 
            return float('inf') 

        common_divisor = math.gcd(side_a, side_b)

        simplified_numerator = side_a // common_divisor
        simplified_denominator = side_b // common_divisor
        
        # Return the ratio as a float based on simplified fraction
        if simplified_denominator == 0:
            return float('inf') 
            
        return simplified_numerator / simplified_denominator

if __name__ == '__main__':
    calculator = GeometryCalculator()

    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (3, 4),   # Classic Pythagorean triple: ratio should be 0.75 simplified from 3/4
        (12, 8),  # Same as above scaled up -> simplifies to same ratio
        (5, 12),  # Another common set
        (1, 1),   # Equal sides -> ratio 1.0
    ]

    for side_a, side_b in test_cases:
        result = calculator.calculate_side_ratio(side_a, side_b)
        print(f"Ratio of {side_a} to {side_b}: {result}")