import math

class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies two weight ratios by dividing both numbers 
        by their greatest common divisor (GCD).
        
        Args:
            ratio_a (int or float): The first value in the ratio.
            ratio_b (int or float): The second value in the ratio.
            
        Returns:
            tuple: A simplified pair of integers representing the ratio.
                   If inputs are floats, they are converted to 
                   rounded integers before processing.
        """
        # Convert inputs to integers if necessary and handle edge cases
        try:
            a = int(round(ratio_a))
            b = int(round(ratio_b))
            
            if a == 0 or b == 0:
                return (a, b)
                
            gcd_value = math.gcd(a, b)
            simplified_a = a // gcd_value
            simplified_b = b // gcd_value
            
            # Ensure the first number is non-negative for consistency
            if simplified_a < 0 and simplified_b < 0:
                return (-simplified_a, -simplified_b)
                
            return (simplified_a, simplified_b)
        except (ValueError, TypeError):
            raise ValueError("Inputs must be numeric values.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = RatioConverter()
    
    test_cases = [
        (10, 20),      # Simple case: should return (1, 2)
        (50, 75),      # Another simple case: should return (2, 3)
        (-4, -8),      # Negative numbers: should return (-1, -2) or equivalent normalized form
        (6.5, 9.5),    # Float inputs that round to integers: 6 and 9 -> GCD is 3 -> (2, 3)
        (0, 5),        # One zero case
        (7, 14),       # Perfect square ratio
    ]
    
    print("Ratio Simplification Results:")
    for i, (r_a, r_b) in enumerate(test_cases):
        simplified = converter.simplify(r_a, r_b)
        original_str = f"{r_a} : {r_b}" if isinstance(r_a, float) or isinstance(r_b, float) else f"{int(r_a)} : {int(r_b)}"
        print(f"Original: {original_str:>10} -> Simplified: {simplified[0]} : {simplified[1]}")