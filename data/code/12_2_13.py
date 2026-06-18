import math

class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies two weight ratios by dividing both numbers by their Greatest Common Divisor (GCD).
        
        Parameters:
            ratio_a (int or float): The first part of the ratio.
            ratio_b (int or float): The second part of the ratio.
            
        Returns:
            tuple[int, int]: A simplified representation of the ratio as a tuple of integers.
        """
        # Convert inputs to integers for GCD calculation
        a = math.floor(ratio_a)
        b = math.floor(ratio_b)

        if a == 0 and b == 0:
            raise ValueError("Ratio cannot be zero.")

        gcd_val = math.gcd(a, b)
        
        return (a // gcd_val, b // gcd_val)

if __name__ == '__main__':
    converter = RatioConverter()

    # Sample test cases with hard-coded values
    sample_ratios = [
        (10, 20),       # Expected: (1, 2)
        (5.4321, 9.6789),   # Truncated to floor for integer handling; Expected: (32, 53) if floored exactly or logic adjusted. 
                          # Assuming standard float input implies converting to int via math.floor as per robustness requirement above.
        (40, 80),       # Expected: (1, 2)
    ]

    for r_a, r_b in sample_ratios:
        simplified = converter.simplify(r_a, r_b)
        print(f"Original Ratio ({r_a}, {r_b}) -> Simplified: {simplified}")