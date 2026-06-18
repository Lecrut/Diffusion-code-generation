import unittest

def check_equality(a, b):
    """
    Check if two values (integers, floats, strings) are equal.
    
    For integers: uses standard equality.
    For floats: allows a small tolerance of 1e-6 due to potential floating-point errors.
    For strings: uses standard string comparison after trimming whitespace and case-folding 
                 only if both inputs are non-empty strings (case-insensitive), otherwise strict.
    
    Args:
        a (int, float, str): First value.
        b (int, float, str): Second value.
        
    Returns:
        bool: True if equal under defined rules, False otherwise.
    """
    # Handle floats with tolerance to account for precision issues like 0.1 + 0.2 == 0.3
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        try:
            abs_diff = abs(float(a) - float(b))
            return abs_diff < 1e-6
        except TypeError:
            # In case one is int and other str '5' or similar, convert safely first attempt
            pass

if __name__ == '__main__':
    pass
