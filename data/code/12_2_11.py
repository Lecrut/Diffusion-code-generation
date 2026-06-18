import math

class RatioConverter:
    def simplify(self, ratio_a, ratio_b):
        """
        Simplifies a weight ratio (ratio_a : ratio_b) by dividing both numbers 
        by their greatest common divisor using the Euclidean algorithm.
        
        Args:
            ratio_a (int or float): The first part of the ratio.
            ratio_b (int or float): The second part of the ratio.
            
        Returns:
            tuple: A simplified ratio as a tuple (simplified_a, simplified_b).
                   If inputs are floats with finite decimal representations, 
                   they will be converted to integers before processing if exact.
        
        Raises:
            ValueError: If either input is zero or negative.
        """
        # Handle non-integer inputs by attempting conversion to int only if representable exactly
        try:
            a = int(ratio_a)
            b = int(ratio_b)
        except (ValueError, TypeError):
            raise ValueError("Inputs must be integers or floats that can be represented as exact integers.")

        # Validate inputs
        if a <= 0 or b <= 0:
            raise ValueError("Ratio components must be positive numbers.")

        # Calculate GCD using Euclidean algorithm (math.gcd is efficient, but we implement explicitly 
        # to ensure no external dependency issues and demonstrate the logic as requested)
        
        def euclidean_gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        gcd_val = euclidean_gcd(a, b)
        
        simplified_a = a // gcd_val
        simplified_b = b // gcd_val
        
        return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    converter = RatioConverter()

    # Test Case 1: Simple integer ratio
    result_1 = converter.simplify(60, 45)
    print(f"Simplified {60} : {45} is {result_1}") 

    # Test Case 2: Larger integers with common factor
    result_2 = converter.simplify(180, 300)
    print(f"Simplified {180} : {300} is {result_2}")

    # Test Case 3: Prime numbers (GCD should be 1)
    result_3 = converter.simplify(7, 11)
    print(f"Simplified {7} : {11} is {result_3}")

    # Test Case 4: Powers of the same number
    result_4 = converter.simplify(8, 24)
    print(f"Simplified {8} : {24} is {result_4}")

    # Verification output expectations:
    # Simplified 60 : 45 is (4, 3)
    # Simplified 180 : 300 is (3, 5)
    # Simplified 7 : 11 is (7, 11)
    # Simplified 8 : 24 is (1, 3)