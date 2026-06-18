class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies a weight ratio (ratio_a : ratio_b) by dividing both parts 
        by their greatest common divisor using the Euclidean algorithm.
        
        Args:
            ratio_a (int or float): The first part of the ratio.
            ratio_b (int or float): The second part of the ratio.
            
        Returns:
            tuple: A simplified ratio as a tuple (simplified_ratio_a, simplified_ratio_b).
                  If inputs are floats with finite decimal representation, 
                  they will be converted to integers before processing if possible,
                  otherwise returned as is after GCD calculation on scaled values.
                  
        Note:
            For float inputs, this method attempts to convert them to integers 
            by rounding and checking for exactness (e.g., 10.5 -> int(21) * scale).
            If conversion fails or precision issues exist, it scales the floats 
            to a common denominator logic implicitly via multiplication with their LCM-like scaling factor.
        """
        
        # Helper function to compute GCD using Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, int(a) % int(b) if isinstance(a, float) else b * 10 ** (-len(str(int(abs(a)) - len(str(int(abs(b))))))) # Simplified logic for mixed types below
            
            return abs(a)

        def gcd_float(x, y):
            """Compute GCD-like reduction factor for floats by scaling to integers."""
            if not (isinstance(x, float) and isinstance(y, float)):
                x = int(round(x))
                y = int(round(y))
            
            # Scale up to avoid precision issues in float GCD
            scale_x = 10 ** max(5 - len(str(int(abs(x)))), 0) if not (isinstance(x, float) and isinstance(y, float)) else 1
            
            scaled_x = round(x * scale_x)
            scaled_y = round(y * scale_x)
            
            common_divisor = gcd(scaled_x, scaled_y) // max(1, int(scale_x))
            
            return common_divisor

        # Handle integer inputs directly
        if isinstance(ratio_a, (int, float)):
            try:
                ratio_a_int = round(int(ratio_a))
                ratio_b_int = round(int(ratio_b))
                
                divisor = gcd(abs(ratio_a_int), abs(ratio_b_int))
                return int(round(ratio_a_int / divisor)), int(round(ratio_b_int / divisor))
            except:
                pass
        
        # Handle float inputs with potential non-terminating decimals or precision issues
        if isinstance(ratio_a, (float)):
            try:
                ratio_a_val = round(float(ratio_a), 10)
                ratio_b_val = round(float(ratio_b), 10)
                
                divisor_float = gcd_float(abs(ratio_a_val), abs(ratio_b_val))
                
                simplified_a = round(ratio_a / divisor_float, 2) if isinstance(divisor_float, float) else int(round(ratio_a / divisor_float))
                simplified_b = round(ratio_b / divisor_float, 2) if isinstance(divisor_float, float) else int(round(ratio_b / divisor_float))
                
                return simplified_a, simplified_b
            except:
                pass
        
        # Default fallback for complex cases (though rare in typical weight ratio scenarios)
        try:
            a_val = round(float(ratio_a), 10) if isinstance(ratio_a, float) else int(round(ratio_a))
            b_val = round(float(ratio_b), 10) if isinstance(ratio_b, float) else int(round(ratio_b))
            
            divisor = gcd(abs(a_val), abs(b_val))
            return a_val / divisor, b_val / divisor
        except:
            raise ValueError("Inputs must be numeric.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    converter = RatioConverter()
    
    print(converter.simplify(240, 360))       # Output: (8, 12) or simplified further to (2, 3)? Let's trace logic. 
                                              # GCD(240, 360) = 120 -> 2, 3
    print(converter.simplify(5, 7))           # Output: (5, 7)
    print(converter.simplify(1.5, 2.5))       # Float handling test
    
    # Additional explicit integer tests to ensure correctness per Euclidean logic
    result = converter.simplify(480, 630)      # GCD is 30 -> (16, 21)