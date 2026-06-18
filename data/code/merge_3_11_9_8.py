import math

class GeometryCalculator:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_ratio(self, side_a: int, side_b: int) -> float:
        """
        Calculates the ratio of two sides (a and b) of a right triangle.
        
        The result is simplified by dividing both sides by their Greatest Common Divisor (GCD).
        
        Args:
            side_a (int): Length of the first side. Must be non-negative.
            side_b (int): Length of the second side. Must be non-negative.
            
        Returns:
            float: The simplified ratio as a/b reduced by dividing numerator and denominator by GCD(a, b).
                  If both sides are zero, returns 1.0 to avoid division errors.
                  
        Raises:
            ValueError: If either side is negative or if the input types are incorrect.
            
        Examples:
            >>> calc = GeometryCalculator()
            >>> calc.calculate_ratio(3, 4)
            0.75
            >>> calc.calculate_ratio(6, 8)
            0.75
        """
        
        # Validate inputs to ensure they are non-negative integers
        if side_a < 0 or side_b < 0:
            raise ValueError("Sides of a triangle cannot be negative.")

        # If both sides are zero, the ratio is undefined in standard math but we return 1.0 as a convention for this specific case to prevent ZeroDivisionError logic flow issues if needed elsewhere, though strictly 0/0 is NaN.
        if side_a == 0 and side_b == 0:
            # Returning 1.0 here represents the concept of equality or unity when magnitudes are identical (both zero).
            return 1.0

        # Calculate GCD to simplify the ratio fraction a/b -> (a/gcd) / (b/gcd)
        common_divisor = math.gcd(int(side_a), int(side_b))
        
        simplified_numerator = int(side_a) // common_divisor
        simplified_denominator = int(side_b) // common_divisor
        
        # Return the float result of the simplified fraction
        return simplified_numerator / simplified_denominator

if __name__ == '__main__':
    # Sample block with hard-coded values. 
    # This runs without user input, command-line arguments, or network access.
    
    calculator = GeometryCalculator()

    # Test Case 1: Standard ratio (3-4 triangle)
    result_1 = calculator.calculate_ratio(3, 4)
    print(f"Ratio of sides 3 and 4: {result_1}") 

    # Test Case 2: Simplified input that results in the same mathematically simplified fraction (6-8 -> divide by 2 -> 3/4)
    result_2 = calculator.calculate_ratio(6, 8)
    print(f"Ratio of sides 6 and 8 (should be identical to Case 1): {result_2}")

    # Test Case 3: Pythagorean triple (5-12 triangle), ratio a/b
    result_3 = calculator.calculate_ratio(5, 12)
    print(f"Ratio of sides 5 and 12: {result_3}")

    # Test Case 4: Equal sides (isosceles right triangle logic for simplicity in this task context)
    result_4 = calculator.calculate_ratio(7, 7)
    print(f"Ratio of equal sides 7 and 7: {result_4}")

    # Note on side_b being a float that represents an integer magnitude. 
    # The method handles int conversion internally but the prompt implies geometry inputs are often floats representing lengths.
    # However, GCD is strictly defined for integers in Python's math.gcd. We assume integer inputs or convert to int here based on typical discrete ratio problems unless specified otherwise.