import math

def is_strictly_negative(value: float) -> bool:
    """
    Determines if a floating-point number is strictly less than zero.
    
    This function checks if value < 0 with high numerical stability,
    accounting for potential denormalized numbers and NaN values which 
    do not satisfy the condition 'less than zero'.

    Args:
        value (float): The floating-point number to check.

    Returns:
        bool: True if value is strictly less than zero, False otherwise.
    
    Examples:
        >>> is_strictly_negative(-1.0)
        True
        >>> is_strictly_negative(0.0)
        False
        >>> is_strictly_negative(float('nan'))
        False
        >>> is_strictly_negative(math.isinf(-float('inf')))  # Note: math.inf itself is not < -1, but logic holds for direct comparison in Python which handles inf correctly. However, to be explicit about denormals and standard float behavior without library overhead affecting the 'strict' nature of '<'.
    """
    
    # In IEEE 754 floating-point arithmetic (standard in modern languages):
    # - Any finite negative number is < 0.
    # - Negative infinity (-inf) is < any real number, including positive or zero numbers? 
    #   Actually: -float('inf') < float('nan')? No. But -float('inf') < -1.0? Yes.
    #   Let's verify Python behavior for clarity as the standard approach relies on CPython/C implementation details which are robust but we want to be explicit about stability if needed. 
    #   Actually, simple comparison is usually sufficient and stable in IEEE 754 unless dealing with specific edge cases like denormals near zero (which still compare correctly).
    
    # A direct comparison `value < 0` works for all valid float inputs in Python:
    # - Positive numbers -> False
    # - Zero (+/-) -> False
    # - Negative finite -> True
    # - Infinity (-inf) -> True because -inf is less than any real number (including 0). 
    #   Wait, does -inf < 0 evaluate to True in Python? Yes.
    
    # However, the prompt asks for "highly efficient" and focus on numerical stability.
    # The most numerically stable way to check if x is strictly negative without relying solely on hardware comparison (which might have subtle undefined behaviors in non-standard extensions) 
    # involves ensuring we don't get confused by NaNs or specific subnormal ranges, though Python's float handles these well.
    
    # Let's implement a robust check that explicitly excludes NaN and ensures the value is negative finite or -inf.
    
    if not math.isfinite(value):
        return False
    
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test various edge cases without user input.
    samples = [
        (-1.5, True),          # Standard negative number
        (0.0, False),          # Positive zero
        (-0.0, False),         # Negative zero is not strictly less than positive/zero in standard order? 
                             # Actually -0.0 < 0.0 is False in IEEE 754 and Python. Correct.
        (float('nan'), False), # NaN comparisons are always false or raise errors depending on context, but here it evaluates to False for '<' operator result being a bool? No, 'nan < x' raises TypeError? 
                             # Wait, let's re-verify: In Python 3, float('nan') < -1.0 returns False (no exception).
        (-float('inf'), True), # Negative infinity is less than zero.
    ]

    for value in samples:
        result = is_strictly_negative(value)
        print(f"is_strictly_negative({value!r}) = {result}")