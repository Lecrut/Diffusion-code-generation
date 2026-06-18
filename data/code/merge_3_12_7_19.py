import math

def convert_weight_ratio(a: int, b: int) -> float:
    """
    Optimized function to compute weight ratio a/b as a float.
    Prioritizes computational speed over readability by using direct division 
    and avoiding unnecessary object creation or complex type conversions.
    
    Args:
        a (int): Numerator of the weight ratio.
        b (int): Denominator of the weight ratio. Must be non-zero.
        
    Returns:
        float: The resulting decimal value of the ratio.
        
    Raises:
        ValueError: If denominator is zero or inputs are not integers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
    
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero in weight ratio conversion.")

    # Direct float division is the fastest method for this specific task.
    return a / b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    
    # Sample 1: Standard integer inputs
    result_1 = convert_weight_ratio(100, 25)
    
    # Sample 2: Large integers (prioritizing speed over arbitrary precision logic here as float is standard for ratios unless specified otherwise)
    large_a = 98765432101234567890
    large_b = 123456789012345
    result_2 = convert_weight_ratio(large_a, large_b)
    
    # Sample 3: Negative integers (valid for ratio calculations in physics/engineering contexts)
    result_3 = convert_weight_ratio(-50, -10)

    # Output results directly to stdout as the module is self-contained.
    print(f"Ratio {result_1}")
    print(f"Large Ratio {result_2:.6f}")
    print(f"Negative Ratio {result_3}")