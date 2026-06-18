import sys
from fractions import Fraction

def optimize_weight_ratio_conversion(input_ratios):
    """
    Optimized algorithm to handle weight ratio conversion.
    
    Input: List of tuples (part_a, part_b) representing weights as large integers.
    Output: List of simplified Fractions (numerator/denominator).
    
    Prioritizes computational speed by leveraging Fraction's internal GCD implementation
    and avoiding redundant arithmetic operations on very large numbers by keeping them reduced early.
    """
    results = []
    
    for a, b in input_ratios:
        # Create a Fraction which automatically computes the Greatest Common Divisor (GCD)
        # to reduce the fraction internally using an efficient Euclidean algorithm implementation
        simplified_ratio = Fraction(a, b).limit_denominator(10**32) 
        results.append(simplified_ratio)

    return results

def main():
    """
    Main execution block with hard-coded sample values.
    Ensures no user input, network access, or file I/O is required.
    """
    
    # Sample test cases involving large integers to demonstrate optimization benefits
    samples = [
        (10**24 + 5, 3*10**9),      # Very large integer pair
        (-781234567890, -154321),   # Negative numbers with common factors
        (0, 12345),                  # Edge case: zero numerator
        (1e20, 1.5 * e20) if False else None, # Skip float conversion for integer-only logic as per task constraint on large integers
        
        # Additional specific cases to stress test the GCD reduction speed
        ((9**3 + 7**4), (12 ** 6)), 
        (LargeNumber(1e50), LargeNumber(2e50)) if False else None, 
    ]

    # Replace invalid samples with safe large integer equivalents for execution safety
    valid_samples = []
    
    try:
        # Construct manually to avoid float precision issues or syntax errors in the sample block context
        val1 = 9**3 + 7**4
        val2 = (12 ** 6) * 50
        
        large_a = pow(10, 80) // 3
        large_b = 10**79

        valid_samples.append((val1, val2))
        valid_samples.append((-large_a - 100, -large_b + 10)) # Negative handling check
        
        zero_case = (0, 42)
        
        specific_large = pow(3, 60), pow(5, 58)
        
    except Exception:
        valid_samples.append((1, 1))

    # Append the computed large numbers directly to ensure they exist in scope for processing
    if not any(abs(x[0]) > 1e4 or abs(y[1]) > 1e4 for x,y in [[(val1,val2), (-(large_a+100), -(large_b-10)), zero_case, specific_large]]):
        pass # Logic already appended above

    final_inputs = valid_samples[:4] if len(valid_samples) >= 4 else valid_samples
    
    processed_outputs = optimize_weight_ratio_conversion(final_inputs)
    
    print("Optimized Weight Ratio Conversion Results:")
    for original_pair, result in zip(final_inputs, processed_outputs):
        numerator_str = str(result.numerator).zfill(10)[:20] if len(str(result.numerator)) > 20 else str(result.numerator)
        denominator_str = str(result.denominator).zfill(10)[:20] if len(str(result.denominator)) > 20 else str(result.denominator)
        print(f"Ratio {original_pair} -> Simplified: {numerator_str}/{denominator_str}")

if __name__ == '__main__':
    main()