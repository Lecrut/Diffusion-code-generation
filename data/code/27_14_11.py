# Check if two floating-point values are different using a tolerance-based approach
def is_different(a: float, b: float) -> bool:
    return abs(a - b) > 1e-9

if __name__ == '__main__':
    val_int = 10
    val_float_approx = 10.00000000000001
    
    # Direct comparison (may fail due to precision limits in some contexts, 
    # though Python floats are usually fine for these specific values).
    direct_result = val_int != val_float_approx
    
    # Tolerance-based check is safer for floating-point arithmetic.
    tolerance_result = not is_different(val_int, val_float_approx)
    
    print(f"Direct comparison result: {direct_result}")
    print(f"Tolerance based difference found: {is_different(val_int, val_float_approx)}")