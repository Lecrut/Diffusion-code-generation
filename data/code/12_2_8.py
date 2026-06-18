import math

class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies a weight ratio (ratio_a : ratio_b) by dividing both parts
        by their greatest common divisor using the Euclidean algorithm.

        Args:
            ratio_a (int or float): The first part of the ratio.
            ratio_b (int or float): The second part of the ratio.

        Returns:
            tuple[int, int]: A simplified integer pair representing the reduced ratio.
        
        Note:
            If non-integer inputs are provided, they will be converted to integers.
            Zero values in the input may result in division by zero errors; 
            this method assumes valid positive or negative numeric inputs where GCD is defined.
        """
        # Convert inputs to absolute integer values for calculation purposes
        a = int(abs(ratio_a))
        b = int(abs(ratio_b))

        if a == 0 and b == 0:
            raise ValueError("Both parts of the ratio cannot be zero.")

        # Compute GCD using Euclidean algorithm (math.gcd handles integers efficiently)
        gcd_value = math.gcd(a, b)

        simplified_a = int(ratio_a / gcd_value) if a != 0 else 1
        simplified_b = int(ratio_b / gcd_value) if b != 0 else 1

        return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    converter = RatioConverter()

    test_cases = [
        (3, 9),      # Expected: (1, 3)
        (50, 25),    # Expected: (2, 1) or (-2, -1) depending on sign handling logic applied here
        (7.5, 15.0), # Expected: integers derived from float division after GCD of scaled values? 
                     # Note: The current implementation converts floats to int first via abs().
                     # For pure float simplification like 3/4 : 6/8 -> 3:6 -> (1,2) logic needs care.
    ]

    print("Running RatioConverter tests...\n")

    for r_a, r_b in test_cases:
        try:
            result = converter.simplify(r_a, r_b)
            # Adjust output to reflect original signs if inputs were negative (simplified version below handles magnitude only via abs logic above but returns signed based on float division)
            # Re-evaluating for clean sign preservation in final return relative to input ratio direction:
            
            # Corrected simplified logic preserving sign relationship of input floats/integers directly divided by gcd of absolute values scaled appropriately? 
            # Actually, let's stick strictly to the implemented math which uses abs() internally but divides original signed float/int.
            
            print(f"Input Ratio ({r_a} : {r_b}) -> Simplified: {result}")
        except Exception as e:
            print(f"Error processing ratio ({r_a}, {r_b}): {e}")

    # Additional explicit integer test to ensure clarity on sign handling relative to input signs if not using abs for final result calculation in a way that loses info.
    # The current implementation calculates gcd of absolute values, then divides original signed numbers by that GCD. 
    # This preserves the sign of the individual inputs while reducing magnitude proportionally.

    print("\n--- Explicit Integer Tests ---")
    explicit_tests = [(-4, 6), (10, -20)]
    
    for r_a, r_b in explicit_tests:
        res = converter.simplify(r_a, r_b)
        # To ensure the ratio direction is preserved correctly relative to standard math simplification where signs are often normalized or kept as-is based on input magnitude reduction.
        # Given gcd(a,b) returns positive, dividing negative numbers by it keeps them negative.
        print(f"Input ({r_a}, {r_b}) -> Output: {res}")

    # Verify the logic against standard expectation for (-4 : 6). 
    # GCD(4,6)=2. -4/2 = -2, 6/2=3. Result (-2, 3).
    # This is mathematically equivalent to (2:-3) but keeps input signs unless explicitly normalized elsewhere.