import math

def is_strictly_negative(x: float) -> bool:
    """
    Determine if a floating-point number is strictly less than zero.
    
    This function checks if x < 0 with high numerical stability, handling 
    standard edge cases like -0.0 correctly (since -0.0 == 0 but is not negative).
    
    Args:
        x (float): The input number to check.
        
    Returns:
        bool: True if x is strictly less than zero, False otherwise.
    """
    # Direct comparison with < handles all IEEE 754 cases correctly for floats.
    # It naturally distinguishes between -0.0 and +0.0 (returns False) 
    # and handles subnormal numbers without special loss of precision logic needed here.
    return x < 0

if __name__ == '__main__':
    # Hard-coded sample values to test various edge cases numerically stable check
    
    samples = [
        -1.5,           # Standard negative number -> True
        -0.0,           # Negative zero is not strictly less than zero -> False
        0.0,            # Positive/Zero -> False
        float('-inf'),  # Negative infinity -> True
        float('inf'),   # Positive infinity -> False
        math.nextafter(0.0, -1.0), # Smallest positive subnormal minus epsilon (if applicable) or just next after 0 towards negative
        
        # Testing with very small numbers close to zero
        1e-308 * (-2**(-1074)), 
    ]

    for val in samples:
        result = is_strictly_negative(val)
        print(f"is_strictly_negative({val}) = {result}")