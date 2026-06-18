import math

def is_strictly_negative(value: float) -> bool:
    """
    Determines if a floating-point number is strictly less than zero.
    
    This function handles potential edge cases related to numerical stability,
    such as NaN and Infinity values, ensuring robust behavior across the 
    entire range of IEEE 754 floating-point numbers.
    
    Args:
        value (float): The input floating-point number to check.
        
    Returns:
        bool: True if value is strictly less than zero, False otherwise.
               This includes cases where value is NaN or positive infinity.
    """
    # Check for negative zero (-0.0), which in Python compares equal to 0.0 but 
    # represents a distinct signed zero that might be considered "negative" depending on context.
    # However, the task asks for strictly less than zero (< 0). In IEEE 754:
    # -0.0 < 0.0 is False in Python because they are equal.
    # We rely on standard comparison operators but add checks for NaN and Infinity 
    # to ensure numerical stability as requested, although math.isfinite() can help here too.
    
    if not isinstance(value, (float, int)):
        raise TypeError("Input must be a numeric type.")

    # Explicitly check for Not-a-Number (NaN). Comparing NaN with anything returns False or raises errors in some contexts? 
    # Actually 'x < 0' where x is NaN evaluates to False. But let's be explicit for clarity and stability.
    if math.isnan(value):
        return False
    
    # Check for positive infinity; it should not be considered less than zero.
    if value == float('inf'):
        return False
        
    # Standard comparison handles negative numbers, -0.0 (which is equal to 0), 
    # and finite negatives correctly in Python's IEEE 754 compliant implementation.
    # The only tricky part usually arises with NaN or infinities which are handled above.
    
    return value < 0

if __name__ == '__main__':
    # Hard-coded sample values to test various edge cases without user input
    
    samples = [
        -1.5,           # Standard negative number -> True
        -0.0,           # Negative zero (mathematically often treated as equal to 0 in comparisons) -> False
        0.0,            # Zero -> False
        float('inf'),   # Positive infinity -> False
        float('-inf'),  # Negative infinity -> True (since -inf < 0 is mathematically true and holds in Python)
        float('nan'),   # NaN -> False
    ]

    for sample in samples:
        result = is_strictly_negative(sample)
        print(f"is_strictly_negative({sample!r}) = {result}")