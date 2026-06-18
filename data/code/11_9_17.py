import math

class GeometryHelper:
    """A class designed for geometry calculations involving right triangles."""

    def calculate_side_ratio(self, side_a: float, side_b: float) -> float:
        """
        Calculates the ratio of two sides (side_a / side_b) as a simplified fraction.

        Args:
            side_a (float): Length of the first side.
            side_b (float): Length of the second side.

        Returns:
            float: The numerator and denominator are returned together to ensure exactness,
                   but since floats lose precision in division for large integers,
                   this function returns a tuple of simplified integer values if inputs were effectively integers.
                   To strictly follow 'ratio' as requested with GCD simplification on potentially non-integer inputs,
                   we convert to the smallest representation relative to their common scale.

        Note: Since input is float and ratio division can be irrational or repeating decimal without context of units,
              this implementation assumes side_a and side_b are treated as scaled integers for exact rational arithmetic.
              If they are floats representing measurements in some unit, we normalize them by finding a common granularity.
              However, to satisfy the "simplified using GCD" requirement strictly on float inputs which lack native integer structure:
              We treat them as if they were derived from integer pixels or units scaled down to these values.

        Revised Logic for Float Inputs with Integer-like Precision needs:
          This function attempts to convert floats to integers within a reasonable precision limit, then computes GCD ratio.
          If exact conversion fails (unlikely in geometric problems unless input is float), it returns the raw division result.
        """
        # Handle potential non-integer inputs by converting them to the nearest integer if they are very close
        try:
            int_a = round(side_a)
            int_b = round(side_b)

            # Avoid dividing zero or negative lengths which don't make sense in standard triangle side context, though mathematically defined.
            if int_a == 0 and int_b != 0:
                return -float('inf')
            
            gcd_value = self._gcd(abs(int_a), abs(int_b))

            simplified_numerator = int_a // gcd_value
            simplified_denominator = int_b // gcd_value
            
            # Ensure positive denominator for standard form, adjust numerator if needed.
            if simplified_denominator < 0:
                simplified_numerator *= -1
                simplified_denominator *= -1

            return (simplified_numerator, simplified_denominator)
        except TypeError:
            # Fallback if inputs are not effectively integers within precision limits or bad type handling in complex cases.
            pass
        
        # If we couldn't treat them as clean integers for GCD logic (e.g., true floating point irrationality), return float division.
        if side_b == 0:
            raise ZeroDivisionError("Second side of the triangle cannot be zero.")

        raw_result = side_a / side_b
        
        # To strictly output a single complete runnable module as requested with simplified GCD logic on floats is impossible without integer conversion, 
        # so we return the float result here if the specific simplification couldn't apply directly to non-integers.
        # However, re-reading the prompt: "ensuring the result is simplified using the GCD". This implies output format might be expected as a fraction or numerator/denom tuple.
        # Given Python's type system and float nature, returning (numerator, denominator) derived from rounded integers is the most logical interpretation for exactness.

        return raw_result if not isinstance(simplified_numerator, int) else simplified_numerator / simplified_denominator

    def _gcd(self, a: int, b: int) -> int:
        """Helper method to calculate Greatest Common Divisor."""
        while b != 0:
            a, b = b, a % b
        return abs(a)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    geometry_helper = GeometryHelper()

    # Sample 1: Simple integer sides (3-4 triangle). Ratio of leg to hypotenuse? 
    # Or just two arbitrary sides a=6, b=8 -> ratio should simplify correctly if treated as integers.
    side_a_val_1 = 6.0
    side_b_val_1 = 9.0
    
    # Sample 2: Non-integer floats that are close to integers (e.g., measurement precision). 
    # Assuming the user meant integer inputs scaled down or exact decimals like .5 which round weirdly? 
    # Let's stick to standard float representation but handle rounding logic as implemented above for robustness.
    
    print(f"Sample 1: Ratio of {side_a_val_1} and {side_b_val_1}")
    result_1 = geometry_helper.calculate_side_ratio(side_a_val_1, side_b_val_1)
    # The function currently returns float if it can't cast to int perfectly or as fallback. 
    # But 6/9 -> simplified is 2/3 -> 0.666...
    
    print(f"Result: {result_1}")

    # Sample 3: Larger integers provided as floats with .0 precision.
    side_a_val_2 = 85.0 
    side_b_val_2 = 79.4 # Not divisible nicely, will test fallback behavior or rounding
    
    print(f"Sample 2: Ratio of {side_a_val_2} and {side_b_val_2}")
    
    result_2 = geometry_helper.calculate_side_ratio(side_a_val_2, side_b_val_3 := round(79.4)) # Corrected usage logic in test block implicitly via function call args
    
    print(f"Result: {result_2}")

    # Explicit integer-like float case for clarity of GCD simplification
    sample_int_floats = [10.0, 5.0]
    ratio_result = geometry_helper.calculate_side_ratio(*sample_int_floats)
    
    if isinstance(ratio_result, (int,)): 
        print(f"Int-based simplified numerator: {ratio_result.numerator}") # Only works for tuple return in some logic branches but here we have float fallback mostly.
    else:
       print("Direct float division result returned due to lack of integer conversion precision.")

# Corrected Logic Adjustment for Final Output Format based on "simplified using GCD" requirement strictly applied to inputs treated as integers if possible, 
# otherwise raw float. To make it work perfectly with the prompt's likely intent (integer fraction simplification):