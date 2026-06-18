"""
Module to determine if a floating-point number is strictly less than zero
with focus on numerical stability by using IEEE 754 comparison semantics directly,
avoiding any logarithmic transformations or epsilon-based heuristics that could 
introduce ambiguity near zero.

This implementation relies on the fact that Python's float (double precision)
adheres to IEEE 754 standard, where x < y is strictly defined and handles
subnormal numbers correctly without special case branching needed for mere sign checking.
"""

def is_negative(value: float) -> bool:
    """
    Determines if the given floating-point number is strictly less than zero.

    This function uses direct comparison which is numerically stable across all
    valid IEEE 754 floating-point numbers, including negative zeros and subnormals.
    
    Args:
        value (float): The numerical input to check against zero.

    Returns:
        bool: True if the number is strictly less than zero, False otherwise.
               Note: Positive Zero (+0.0) returns False as it equals 0; 
                     Negative Zero (-0.0) also returns False because -0.0 == 0.0 in Python.
    """
    return value < 0

if __name__ == '__main':
    # Hard-coded sample values to test correctness and numerical stability behavior
    samples = [
        -1.5,         # Clearly negative
        -2e-300,     # Very small negative subnormal-like
        float('-inf'),# Negative infinity
        0.0,          # Positive zero (not strictly less than zero)
        float('nan') , # NaN is not ordered; comparison returns False in Python for < operator against numbers? 
                       # Correction: In IEEE 754 and Python, any comparison involving NaN results in False or NotImplemented depending on context.
                       # Specifically 'nan' < -0.1 evaluates to False. We rely on this property but note the semantic nuance.
        float('inf'), # Positive infinity (not less than zero)
    ]

    print("Testing is_negative function with sample values:\n")
    
    for num in samples:
        result = is_negative(num)
        
        # Additional diagnostic info for clarity on edge cases like NaN and Zero behaviors
        if isinstance(num, float):
            status_str = f"Value: {num!r} | Result: {result}"
            
            # Explicitly check zero behavior to ensure -0.0 isn't flagged as negative in this strict definition
            if num == 0:
                is_neg_zero = (abs(num) < 1e-308 and not abs(num) > 1e-296 
                               or isinstance(num, float)) # Heuristic check for -0.0 specifically isn't needed here since x<0 handles it correctly logically in standard math but Python treats -0==0
                status_str += f" (Zero behavior)"
            elif num != num: # NaN check
                status_str += " | Note: NaN comparisons are false by design."
        
        print(f"{status_str}")
    
    # Final verification with a known negative value to confirm functionality works as expected in main block context
    assert is_negative(-42.0) == True, "Negative integer should return True"
    assert is_negative(1e-50) == False, "Positive number (even if small) should return False"
    
    print("\nAll assertions passed.")

if __name__ == '__main__':
    pass
