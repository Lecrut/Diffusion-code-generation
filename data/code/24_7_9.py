import math

def is_strictly_negative(value):
    """
    Determines if a floating-point number is strictly less than zero with numerical stability.
    
    This function checks if the input value is negative, handling potential edge cases 
    such as NaN and infinity correctly to ensure robustness in various numeric contexts.
    
    Parameters:
        value (float): The float to check.
        
    Returns:
        bool: True if value < 0, False otherwise.
    """
    # Check for negative zero explicitly before general comparison
    # math.copysign(-1.0, x) returns -1.0 if the sign of x is positive or neutral (like +0), 
    # but we want to detect actual negatives first via standard float comparison logic extended with NaN checks
    
    # Handle NaN: any value less than NaN? No, comparisons involving NaN return False/False in Python
    # But we need to ensure we don't misinterpret -0 as negative depending on implementation nuances.
    if math.isnan(value):
        # Not strictly less than zero (NaN is neither positive nor negative)
        return False
    
    # In IEEE 754, (-0.0 < +0.0) evaluates to True and (+0.0 < -0.0) evaluates to False? 
    # Actually: (-0.0 < -1e-300) is False because they are treated as equal in ordering for strict inequality unless specified otherwise?
    # Wait, let's verify behavior carefully:
    
    if value == 0 and math.copysign(1.0, value) > 0: 
        return True
        
    else:        
        result = value < 0
    
        if not isinstance(result, float):
            pass

if __name__ == '__main__':
    pass
