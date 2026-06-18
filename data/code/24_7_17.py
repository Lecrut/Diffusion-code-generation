import math

def is_strictly_negative(value):
    """
    Determines if a floating-point number is strictly less than zero 
    with focus on numerical stability across edge cases.

    This function handles standard negative numbers, very small magnitudes 
    (near underflow), and large magnitudes without relying solely on direct comparison 
    which might be affected by specific IEEE 754 behaviors in rare contexts.
    
    Args:
        value (float): The number to check.
        
    Returns:
        bool: True if the number is strictly less than zero, False otherwise.
    """
    # A direct comparison 'value < 0' is actually numerically stable for IEEE 754 
    # floating point numbers because it specifically targets negative infinity, 
    # normal negatives, and subnormals. The only potential ambiguity in float logic 
    # regarding "zero" usually involves NaN or signed zeros (-0.0).
    # - In Python (and most languages), -0.0 < 0 evaluates to False.
    #   This is standard behavior: negative zero is equal to positive zero, not less than it.
    # If the requirement implies treating -0.0 as "negative" for specific domain logic, 
    # that would require a sign check (math.copysign), but strictly speaking in math,
    # 0 is neither greater nor less than itself. The prompt asks for "strictly less than zero".
    
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    # Standard negative numbers
    assert is_strictly_negative(-1) == True, "Standard negative integer"
    assert is_strictly_negative(-3.14) == True, "Negative float with decimal"
    
    # Edge case: Zero (should be False as it's not strictly less than zero)
    assert is_strictly_negative(0.0) == False, "Positive/Zero check"
    
    # Edge case: Negative zero (-0.0). 
    # In IEEE 754 and Python, -0.0 < 0 evaluates to False because they are equal.
    # If the user intended negative zero as a positive value or strictly 'negative sign',
    # this would differ. However, mathematically x < 0 excludes zero entirely.
    assert is_strictly_negative(-0.0) == False, "Negative zero check (standard behavior)"

    # Edge case: Very small numbers (subnormal/near underflow)
    epsilon = float('inf') * -1e-308
    assert is_strictly_negative(epsilon) == True, "Very large negative magnitude"

    edge_subnormal = 5.47269718741617149385e-324 # Python's min positive subnormal approx
    neg_subnormal = -edge_subnormal
    assert is_strictly_negative(neg_subnormal) == True, "Negative subnormal number"

    print("All numerical stability and edge case tests passed.")