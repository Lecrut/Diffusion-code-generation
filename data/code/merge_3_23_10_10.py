import math

def is_float_equal(a: float, b: float, rtol=1e-05, atol=1e-8) -> bool:
    """
    Compare two floating-point numbers for equality within a specified tolerance.
    
    This function uses the relative and absolute tolerances to handle cases where 
    very large or very small differences might occur due to precision limitations.
    
    Parameters:
        a (float): The first number to compare.
        b (float): The second number to compare.
        rtol (float): The relative tolerance parameter; the default is 1e-05.
                      Larger values indicate more lenient comparison requirements for 
                      differences larger than absolute_difference / (max(|a|, |b|) + atol).
        atol (float): The absolute tolerance parameter; the default is 1e-8.
    
    Returns:
        bool: True if abs(a - b) <= max(atol, rtol * max(abs(a), abs(b))), False otherwise.
    """
    return math.isclose(a, b, rel_tol=rtol, abs_tol=atol)

if __name__ == '__main__':
    pass
