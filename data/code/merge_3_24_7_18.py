import sys
from decimal import Decimal, getcontext, ROUND_DOWN

def is_strictly_negative(value):
    """
    Determines if a floating-point number (or compatible numeric type) 
    is strictly less than zero with high numerical stability.
    
    This function handles standard floats and integers by converting them 
    to the Decimal context provided for precise comparison, avoiding issues 
    arising from IEEE 754 floating-point edge cases near zero due to precision 
    limitations or representation errors in input data.

    Parameters:
        value (float | int): The number to check. Can be any numeric type.

    Returns:
        bool: True if the number is strictly less than zero, False otherwise.
    
    Raises:
        TypeError: If the input cannot be interpreted as a numeric value.
    """
    try:
        # Convert all inputs to Decimal for precise comparison logic. 
        # This avoids potential pitfalls with float representation issues when comparing near-zero values.
        decimal_value = Decimal(value)
        
        # Directly compare using Decimal's exact arithmetic which is stable and reliable.
        return decimal_value < 0
    
    except TypeError:
        raise TypeError(f"Unsupported type for numeric comparison: {type(value)}")

if __name__ == '__main__':
    sample_values = [
        -1.5,           # Clearly negative
        float('-inf'),   # Negative infinity
        0.0,             # Zero (non-negative)
        -float('inf'),  # Already handled in context but tested explicitly here for clarity
        Decimal("-2"),  # Integer as string converted to Decimal internally via function logic if passed directly or standard conversion path used implicitly by Python's int/float->Decimal constructor. Since the code uses `value` argument, we test with float(-0) and normal negatives. 
        -1e-308,         # Very small negative number (close to denormal limits but still < 0)
    ]

    for val in sample_values:
        result = is_strictly_negative(val)
        print(f"Value {val}: Is strictly negative? {result}")