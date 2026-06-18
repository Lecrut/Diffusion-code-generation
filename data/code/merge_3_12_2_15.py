import math

class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies a weight ratio (ratio_a / ratio_b) to its lowest terms.
        
        Uses the Euclidean algorithm via gcd from the standard library 
        to efficiently find the greatest common divisor and divide both parts by it.

        Args:
            ratio_a (int or float): The numerator of the ratio.
            ratio_b (int or float): The denominator of the ratio.

        Returns:
            tuple[int, int]: A tuple containing the simplified integer values 
                            for the new numerator and denominator after conversion 
                            to integers if necessary before simplification.
        
        Note: This method converts inputs to floats first to handle potential floating-point ratios,
              then multiplies by a scaling factor (1e6) to convert back to large integers 
              where precision is maintained without losing significant digits during integer division.
        """
        # Handle zero denominator case
        if ratio_b == 0:
            raise ValueError("Denominator cannot be zero.")

        # Convert inputs to float for consistent handling of potential decimal ratios
        a = float(ratio_a)
        b = float(ratio_b)

        # Scale up by 1e6 and round to nearest integer to avoid floating-point precision issues 
        # when dealing with very small decimals, then convert back to int. This ensures we work 
        # in the domain of integers for the GCD calculation while preserving relative ratios accurately.
        scaled_a = round(a * 1_000_000)
        scaled_b = round(b * 1_000_000)

        if scaled_a < 0:
            return (-scaled_a, -scaled_b)

        # Compute GCD using Euclidean algorithm logic available in the standard library math module
        gcd_val = self._euclidean_gcd(scaled_a, scaled_b)

        simplified_num = int(round((a / b) * gcd_val)) if a == 0 else (int(a // gcd_val), int(b // gcd_val))
        
        # Correct logic: divide the original float ratio by its GCD equivalent derived from scaled values
        gcd_float = math.gcd(int(abs(scaled_a)), int(abs(scaled_b)))
        simplified_num, simplified_denom = round((a / b) * (gcd_float / 1_000_000)) if a != 0 else (0, 1), \
            round(1.0 / ((a/b)*(gcd_float/1_000_000)))

        # Final simplified tuple based on original float ratio divided by the effective GCD in decimal form
        return int(round((scaled_a // gcd_val))), int(round((scaled_b // gcd_val))) if scaled_b != 0 else (int(scaled_a), 1)

    def _euclidean_gcd(self, a: int, b: int):
        """Helper method to compute GCD using the Euclidean algorithm."""
        while b:
            a, b = b, a % b
        return abs(a)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    converter = RatioConverter()

    test_cases = [
        (100, 25),      # Expected: (4, 1)
        (3.75, 1.5),    # Expected: (5/2 -> scaled and handled appropriately)
        (-6, -9),       # Negative inputs should yield positive simplified ratio or consistent sign handling
        (0, 8),         # Zero numerator case
        (1, 4),         # Simple unit fraction
        (7.3333, 2.5), # Floating point input approximation test
    ]

    print("Running RatioConverter tests...")
    for i, (a_val, b_val) in enumerate(test_cases):
        try:
            result = converter.simplify(a_val, b_val)
            print(f"Test Case {i+1}: simplify({a_val}, {b_val}) -> {result}")
        except Exception as e:
            print(f"Error in Test Case {i+1}: {e}")

    # Verify specific known case manually if needed for clarity during execution trace
    sample = converter.simplify(2, 4)
    assert sample == (1, 2), f"Failed assertion on simple ratio. Got: {sample}"
    print("All assertions passed.")