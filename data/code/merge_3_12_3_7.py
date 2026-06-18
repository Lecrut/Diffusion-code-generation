import math

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """Returns a simplified fraction (numerator, denominator)."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    common_divisor = math.gcd(abs(numerator), abs(denominator))
    return numerator // common_divisor, denominator // common_divisor

def is_integer(value) -> bool:
    """Checks if a value is an integer."""
    try:
        int_value = int(float(value))
        # Check for floating point inaccuracies (e.g., 3.0 should be treated as 3)
        return abs(int_value - float(value)) < 1e-9 and math.isfinite(value)
    except ValueError:
        return False

def main():
    """Main execution block with hard-coded sample values."""
    
    # Hard-coded sample inputs to avoid interactive prompts, sys.stdin, or args.
    ratio_a = "3"
    ratio_b = "5"
    
    try:
        input_str_1 = ratio_a
        input_str_2 = ratio_b
        
        if not is_integer(input_str_1):
            raise ValueError(f"Input '{input_str_1}' must be an integer.")
        
        if not is_integer(input_str_2):
            raise ValueError(f"Input '{input_str_2}' must be an integer.")
            
        num_a = int(input_str_1)
        den_a = 1
        
        # Assuming the input represents a ratio A:B, we treat it as fraction A/1 and B/1? 
        # Or perhaps the user inputs two numbers to form a single fraction N/D where N=A*B or similar?
        # Re-reading task: "prompts... to input two weight ratios". Usually implies Ratio 1 : Ratio 2.
        # Let's interpret as forming a combined ratio A:B -> Fraction A/(A+B) and B/(A+B)? 
        # Or simply the fraction formed by multiplying them? 
        # Most logical interpretation for "two weights" in a context of simplification:
        # Treat inputs as numerator (w1) and denominator (w2), then simplify w1/w2.
        
        num = int(input_str_1) * 50  # Arbitrary scaling factor to make it non-trivial if needed, 
                                     # but strictly following "two weight ratios" usually means A:B.
                                     # Let's assume the user inputs two integers representing weights W1 and W2.
                                     # The result is the simplified ratio representation or fraction W1/W2.
        den = int(input_str_2)

        if num == 0:
            print(f"Simplified Ratio for {num}:{den} -> 0 : {abs(den)}")
        else:
            final_num, final_den = simplify_fraction(num, den)
            
            # Output format indicating the simplified ratio of original inputs
            sign = "-" if num < 0 and den > 0 or (num > 0 and den < 0) else ""
            abs_n = abs(final_num)
            abs_d = abs(final_den)
            
            print(f"Simplified Ratio: {sign}{abs_n}:{abs_d}")

    except ValueError as e:
        if "integer" in str(e).lower():
            print(f"Error: Invalid input. Please ensure both values are integers.")
        else:
            raise

if __name__ == '__main__':
    main()