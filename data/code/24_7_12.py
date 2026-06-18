import math
from decimal import Decimal, getcontext, ROUND_DOWN

def is_strictly_negative(value):
    """
    Determines if a given floating-point number (or numeric type) 
    is strictly less than zero with high numerical stability.
    
    This function handles edge cases such as NaN and Infinity correctly.
    It avoids direct subtraction or multiplication that might introduce precision errors,
    instead relying on the standard comparison operators which are IEEE 754 compliant.
    
    Args:
        value (float|int|Decimal): The number to check.
        
    Returns:
        bool: True if the number is strictly less than zero, False otherwise.
               Returns False for NaN and positive infinity.
    """
    # Handle Decimal types explicitly to ensure precision consistency across numeric bases
    if isinstance(value, Decimal):
        return value < 0
    
    # Convert float/int to a high-precision context for robust comparison logic
    getcontext().prec = 53  # Match double precision capability of standard floats
    
    try:
        decimal_value = Decimal(str(float(value)))
        
        # Explicitly check conditions in order of numerical stability importance
        if math.isnan(decimal_value):
            return False
        
        if math.isinf(decimal_value) and decimal_value > 0:
            return False
            
        # Standard comparison is numerically stable for IEEE 754 floats
        # The only potential instability arises with NaN comparisons, handled above.
        return decimal_value < Decimal(0)
    
    except (ValueError, OverflowError):
        # Fallback to direct float logic if conversion fails or overflows unexpectedly
        try:
            f_val = float(value)
            return math.isnan(f_val) is False and f_val < 0.0
        except Exception:
            return False

if __name__ == '__main__':
    # Hard-coded sample values to test numerical stability without user input
    
    test_cases = [
        -1.5,           # Standard negative float
        -2e-309,        # Very small negative number (near underflow limit)
        0.0,            # Zero (not strictly less than zero)
        1e+308,         # Large positive number
        math.inf,       # Positive infinity
        -math.inf,      # Negative infinity -> Should be True
        float('nan'),   # NaN -> Should be False (NaN is not < 0)
    ]
    
    for test_val in test_cases:
        result = is_strictly_negative(test_val)
        print(f"Input: {test_val!r} | Result: {result}")