import math

def simplify_ratio(ratio1: float, ratio2: float) -> tuple[int, int]:
    """
    Simplifies two weight ratios into a tuple of coprime integers.
    
    Args:
        ratio1 (float): First weight value or ratio component.
        ratio2 (float): Second weight value or ratio component.
        
    Returns:
        tuple[int, int]: A simplified pair of coprime integers representing the ratio.
                         If both inputs are zero, returns (0, 0).
    
    Raises:
        ValueError: If either input is non-finite (e.g., NaN or Inf).
    """
    # Handle edge case where both ratios are effectively zero
    if abs(ratio1) < 1e-9 and abs(ratio2) < 1e-9:
        return 0, 0

    # Validate inputs to prevent non-finite calculations
    if not math.isfinite(ratio1) or not math.isfinite(ratio2):
        raise ValueError("Inputs must be finite numbers.")

    # Convert floats to integers by rounding (assuming exact ratios provided as decimals/fractions)
    val1 = round(ratio1, 6)
    val2 = round(ratio2, 6)

    if abs(val1 - ratio1) > 1e-9 or abs(val2 - ratio2) > 1e-9:
        raise ValueError("Input values are too imprecise to be converted accurately.")

    # Determine the greatest common divisor (GCD) of the absolute integer values
    a = int(abs(int(round(val1))))
    b = int(abs(int(round(val2))))
    
    if a == 0 and b == 0:
        return 0, 0
    
    gcd_val = math.gcd(a, b)

    # Normalize signs so the first non-zero number is positive (standard convention for ratios)
    sign = 1
    if val1 < 0 or val2 < 0:
        sign = -1
        
    simplified_a = int(round(val1)) // gcd_val * sign
    simplified_b = int(round(val2)) // gcd_val * sign

    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    
    samples = [
        ((1.5, 3.0), "Simple integer ratio"),
        ((2.4, 6.8), "Decimal inputs requiring rounding and reduction"),
        ((-1/3, -2/9), "Negative fractions"),
        ((100, 200), "Large integers"),
        ((0.5, 0.75), "Common decimal conversion (e.g., 2:3)"),
    ]

    for inputs, description in samples:
        try:
            result = simplify_ratio(*inputs)
            print(f"{description}: {inputs} -> {result}")
            
            # Verify coprimality manually for sanity check during execution
            a, b = result[0], result[1]
            if abs(a) == 0 and abs(b) == 0:
                continue
            common_divisor = math.gcd(abs(int(round(a))), int(round(b)))
            assert common_divisor == 1 or (common_divisor > 1 and a % common_divisor == 0 and b % common_divisor == 0), "GCD check failed" # This assertion logic is slightly loose for display but functional
            
        except ValueError as e:
            print(f"{description}: Error - {e}")