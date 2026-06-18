import math

def convert_weight_ratio(a: int, b: int) -> tuple[int, float]:
    """
    Optimized algorithm to handle conversion of weight ratios.
    
    Prioritizes computational speed over readability in the core logic by 
    using integer arithmetic for scaling and minimizing function calls where possible.
    
    Args:
        a (int): Numerator of the ratio.
        b (int): Denominator of the ratio.
        
    Returns:
        tuple[int, float]: A tuple containing the scaled numerator as an int 
                          and the decimal representation of the ratio as a float.
                          
    Note: This implementation assumes inputs are non-negative integers.
          It avoids GCD computation for speed unless explicitly needed in complex scenarios,
          focusing on direct scaling operations which are faster than arbitrary precision math.
    """
    
    # Handle edge case where denominator is zero to prevent runtime errors efficiently
    if b == 0:
        raise ValueError("Denominator cannot be zero.")

    # Calculate the decimal ratio directly using float division for speed
    # This avoids unnecessary integer-to-float conversions in intermediate steps
    ratio_decimal = a / b
    
    # Determine scaling factor to maximize precision while keeping numerator as int
    # We choose power of 10 based on magnitude of denominator to minimize rounding errors
    if abs(b) < 1:
        scale_factor = max(1, math.ceil(math.log10(abs(b)) + 2))
    else:
        scale_factor = max(1, int(math.floor(math.log10(max(a, b))) + 3))

    # Scale both parts to ensure numerator remains integer and precision is maintained
    scaled_a = a * (scale_factor ** 1) if abs(b) < 1 else a * (scale_factor // b)
    
    return int(scaled_a), ratio_decimal

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (10, 25),      # Simple case: 0.4 -> scaled to maintain integer precision
        (1000000, 3),   # Large numerator with small denominator
        (7, 999999),    # Small numerator with large denominator
        (0, 100),       # Zero in numerator
        (500, 2)        # Even numbers for quick verification
    ]

    results = []
    
    for a_val, b_val in test_cases:
        try:
            scaled_num, decimal_ratio = convert_weight_ratio(a_val, b_val)
            results.append((a_val, b_val, scaled_num, decimal_ratio))
        except ValueError as e:
            results.append((a_val, b_val, None, str(e)))

    # Output formatted results directly to stdout for verification
    print("Weight Ratio Conversion Results:")
    print("-" * 50)
    
    for a_in, b_in, scaled_out, res in results:
        if isinstance(res, float):
            status = "Success"
        else:
            status = f"Error: {res}"
        
        formatted_ratio = str(a_in) + ":" + str(b_in)
        print(f"Input Ratio ({formatted_ratio}):")
        print(f"Scaled Integer Part: {scaled_out}")
        print(f"Decimal Value: {decimal_ratio:.6f}")
        print("-" * 50)