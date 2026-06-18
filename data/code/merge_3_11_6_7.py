import math

def calculate_ratio(a: int, b: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two potentially large integers a and b.
    
    The function returns a tuple (numerator, denominator) such that 
    numerator / denominator == original_a / original_b in their simplest form.
    
    Args:
        a (int): The first integer. Can be positive, negative, or zero.
        b (int): The second integer. Must not be zero to avoid division by zero logic errors internally.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
                         If both inputs are 0, returns (1, 1) as a mathematical convention for indeterminate forms 
                         or can return (0, 1). Here we handle sign normalization such that denominator is positive.
    """
    
    # Handle case where b is zero to prevent division by zero in GCD calculation if needed later logic changes
    # Though math.gcd handles negative numbers correctly, let's ensure robustness.
    if b == 0:
        # If b is 0 and a is also 0, undefined ratio (returning 1/1 as neutral or raising error could be debated)
        # For this task focusing on simplification logic: return (a // abs(a), 1) if a!=0 else (1, 1)
        if a == 0:
            raise ValueError("Cannot calculate ratio for two zeros.")
        
        sign = -1 if a < 0 else 1
        return (sign * abs(a), 1)

    # Ensure inputs are integers as per requirement. Though Python handles large ints automatically, we assume int type.
    
    # Compute the Greatest Common Divisor
    gcd_value = math.gcd(abs(a), abs(b))

    # Divide both by their GCD to simplify the ratio
    simplified_numerator = a // gcd_value
    simplified_denominator = b // gcd_value

    # Normalize signs: ensure denominator is positive. 
    if simplified_denominator < 0:
        simplified_numerator *= -1
        simplified_denominator *= -1
    
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing the function without any user input or external dependencies.
    
    test_cases = [
        ((4, 6), "Simple even numbers"),          # Should result in (2, 3)
        ((10**50 + 7, -5 * 10**50), "Large positive and negative numbers"), 
        ((-8, 12), "Negative numerator"),         # Should result in (-2, 3) -> normalized to (-2/3)? Actually logic ensures denominator > 0.
             # Wait: -8 / 12 = -2/3. My normalization keeps sign on num if den is pos. 
             # Let's trace: gcd=4 => (-2, 3). Denom positive. OK.
        ((5 * (1 + 7**60), 9), "Very large prime-ish numbers"),
    ]

    for inputs in test_cases:
        a, b = inputs[0]
        description = inputs[1] if isinstance(inputs, tuple) and len(inputs) > 1 else f"a={a}, b={b}"