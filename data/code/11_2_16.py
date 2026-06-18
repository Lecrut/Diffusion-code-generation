import math

class RatioCalculator:
    def simplify_ratio(self, num1, num2):
        """
        Computes the ratio of num1 to num2 in its lowest terms using GCD.
        
        Args:
            num1 (int or float): The numerator value.
            num2 (int or float): The denominator value.
            
        Returns:
            tuple: A tuple containing two integers representing the simplified 
                   ratio (numerator, denominator). If inputs are zero or invalid,
                   appropriate behavior is handled to avoid division by zero errors.
        """
        # Handle cases where input might not be an integer initially
        num1 = int(num1) if isinstance(num1, float) else num1
        num2 = int(num2) if isinstance(num2, float) else num2
        
        # If denominator is 0, return None or a specific indicator to avoid division by zero logic errors later
        if num2 == 0:
            raise ValueError("Denominator cannot be zero.")

        common_divisor = math.gcd(abs(num1), abs(num2))
        
        simplified_numerator = num1 // common_divisor
        simplified_denominator = num2 // common_divisor
        
        # Ensure the denominator is positive for standard form representation
        if simplified_denominator < 0:
            simplified_numerator = -simplified_numerator
            simplified_denominator = -simplified_denominator
            
        return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        30,          # Simplify ratio of 12/6 -> should be 2:1 if using num1=12, num2=6 but here just testing logic with provided inputs
        48,           # Example pairs will follow below for demonstration
        
        # Explicit test cases to run directly in this block
    ]

    # Define a set of explicit sample ratios to simplify and print results
    
    samples = [
        (12, 6),      # Expected: (2, 1)
        (-8, 4),      # Expected: (-2, 1)
        (90, -30),    # Expected: (-3, -1) -> normalized to (-3, -1) or handled sign logic correctly
    
        ]

    calculator = RatioCalculator()

    for i in range(0, len(samples), 2):
        if i + 1 < len(samples):
            num1, num2 = samples[i], samples[i+1]
            try:
                result_numerator, result_denominator = calculator.simplify_ratio(num1, num2)
                print(f"Ratio of {num1} to {num2}:")
                print(f"Simplified Ratio ({result_numerator}, {result_denominator})")
                
                # Verify correctness with a simple check if needed (optional internal logic for verification)
            except ValueError as ve:
                print(f"Error processing ratio {num1}/{num2}: {ve}")
        else:
            break

    # Additional standalone test to ensure no external dependencies or inputs are triggered
    
    final_test = calculator.simplify_ratio(48, 60)
    print("\nFinal Test Case - Ratio of 48/60:")
    print(f"Simplified Result: {final_test}")