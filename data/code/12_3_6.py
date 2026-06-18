import math

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def simplify_ratio(numerator: float, denominator: float) -> tuple[int, int]:
    """Simplify two floating point numbers to their simplest integer ratio.

    Handles cases where inputs are not exact integers by rounding 
    based on proximity and then simplifying the resulting integers.
    
    Args:
        numerator: The first weight value.
        denominator: The second weight value.
        
    Returns:
        A tuple (a, b) representing the simplified ratio a/b in lowest terms.
    """
    # Check if inputs are effectively zero to avoid division by zero errors
    if abs(denominator) < 1e-9 and numerator != 0:
        return (int(numerator), 1)
    
    try:
        num = int(round(numerator))
        den = int(round(denominator))
        
        # If rounding resulted in zero for denominator, handle it as a special case
        if den == 0 and abs(num) > 1e-9:
            return (int(abs(num)), -1 * sign_check(int(num)))

        common = gcd(num, den)
        simplified_num = num // common
        simplified_den = den // common
        
        # Ensure the denominator is positive for standard form representation
        if simplified_den < 0:
            simplified_num *= -1
            simplified_den *= -1
            
        return (simplified_num, simplified_den)
    except Exception as e:
        raise ValueError(f"Error processing inputs: {e}")

def sign_check(value: int) -> int:
    """Helper to determine the correct negative representation."""
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input
    ratio_1 = 3.5
    ratio_2 = 7
    
    try:
        result_num, result_den = simplify_ratio(ratio_1, ratio_2)
        
        if result_den != 0:
            print(f"Input Ratio {ratio_1} : {ratio_2}")
            print(f"Simplified Result: {result_num}/{abs(result_den)}")
        else:
            # Handle case where denominator is zero (infinite ratio)
            print("Result represents an infinite value.")
    except ValueError as ve:
        print(str(ve))