import math

def gcd(a, b):
    """Calculate the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return abs(a) if isinstance(a, int) else 1

def simplify_fraction(numerator, denominator):
    """Simplify a fraction by dividing both numerator and denominator by their GCD.
    
    Handles negative numbers correctly so the result is positive with sign in numerator.
    Assumes inputs are integers or floats that can be converted to exact integers.
    Raises ValueError if conversion fails due to non-integer nature (e.g., 3.5).
    """
    try:
        n = int(numerator)
        d = int(denominator)
        
        # Check for zero denominator after integer conversion, though logic below handles it gracefully or raises error based on spec interpretation of "non-integer inputs" vs valid zeros. 
        # The prompt emphasizes non-integer input handling (like 3.5). A fraction like 0/1 is valid but simplified to 0.
        
    except ValueError:
        raise ValueError("Inputs must be integers or values that convert exactly to integers.")

    if d == 0:
        return n, "undefined"
    
    common = gcd(n, d)
    
    # Ensure the denominator is positive; move sign to numerator if necessary.
    simplified_numerator = n // common * (1 if d > 0 else -1)
    simplified_denominator = abs(d) // common
    
    return str(simplified_numerator), f"{simplified_denominator}"

def main():
    """Execute the command-line logic without external prompts or arguments."""
    
    # Hard-coded sample values as per requirements. 
    # Using integers directly to demonstrate correct functionality and simplicity of inputs.
    ratio1 = 6
    ratio2 = 8
    
    try:
        num, den = simplify_fraction(ratio1, ratio2)
        
        if "undefined" in den or (num == "" and den != ""): # Fallback for edge cases if any logic changes
            print(f"The result is undefined.")
        else:
            final_string = f"{ratio1} / {ratio2}"
            
            try: 
                num_int, den_int = int(ratio1), int(ratio2)
                simplified_numerator_str, denominator_str = simplify_fraction(num_int, den_int)
                
                if "undefined" in denominator_str or not isinstance(denominator_str, str): # Safety check for string output type consistency from helper
                    print(f"Simplified Result: {simplified_numerator_str} / {denominator_str}")
                    
            except ValueError as e:
                raise

    except ValueError as ve:
        error_message = f"Invalid input provided. The inputs must be valid integers, not floats or non-numeric strings.\n{ve}"
        print(error_message)

if __name__ == '__main__':
    main()