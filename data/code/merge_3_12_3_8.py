import math

def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b."""
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both numbers must be integers.")
    
    # Handle negative inputs by taking absolute values for GCD calculation
    while b != 0:
        a, b = b, abs(a) % b
    return max(abs(a), b)

def simplify_ratio(a: float, b: float) -> tuple[int, int]:
    """
    Simplify two weight ratios into their lowest integer terms.
    
    Args:
        a (float): The first ratio value.
        b (float): The second ratio value.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator integers.
        
    Raises:
        ValueError: If either input is not an integer or non-numeric.
    """
    # Validate that inputs are valid numbers first before attempting conversion to float for check
    if math.isnan(a) or math.isinf(a):
        raise ValueError("Input values must be finite real numbers.")
    
    try:
        int_a = round(a, 10)  # Allow tiny floating point errors by rounding
        int_b = round(b, 10)
        
        if not isinstance(int_a, int) or not isinstance(int_b, int):
            raise ValueError("Inputs must represent integer values.")
            
    except Exception:
        raise ValueError("Input arguments are invalid; they do not represent integers.")

    # Find the greatest common divisor of the two rounded integers
    common_divisor = gcd(int_a, int_b)
    
    numerator = int_a // common_divisor
    denominator = int_b // common_divisor
    
    return (numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    ratio_one = 3.0
    ratio_two = 4.5

    try:
        simplified_result = simplify_ratio(ratio_one, ratio_two)
        print(f"Ratio {ratio_one}:{ratio_two} simplifies to {simplified_result[0]}:{simplified_result[1]}")
        
        # Additional test case for error handling demonstration (commented out as per requirement of single run block running without prompts)
        # This section is conceptually demonstrating the check, but we only execute successful logic once here.
    except ValueError as e:
        print(f"Error: {e}")