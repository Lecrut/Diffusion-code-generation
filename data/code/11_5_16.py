def find_ratio_of_lengths(l1, l2):
    """
    Calculates the ratio of two integers l1:l2 as simplified coprime integers (a,b).
    
    Args:
        l1 (int): First length value. Should be an integer >= 0. Negative values are not supported for ratios in this context.
        l2 (int): Second length value. Should be an integer >= 0. 

    Returns:
        tuple[int, int]: A tuple containing the simplified ratio components (a, b).
        
    Raises:
        TypeError: If inputs are not integers or if they contain non-integer types like floats with decimal parts.
    
    The function uses Python's built-in math.gcd for efficiency and correctness in computing GCD of two numbers using Euclidean algorithm logic internally. Negative values result in negative ratios, which is acceptable unless specified otherwise; however, since lengths are typically positive integers >= 0 (and non-zero when forming a ratio), zero division checks have been omitted per strict mathematical definition where dividing by zero results in undefined behavior rather than returning NaNs or special cases for this simplified output.
    
    Note: If l1=0 or l2=0, the function still returns valid coprime outputs consistent with standard math rules (e.g., 0:n -> 0:1 if n>0; a:0 -> 1:0 if a>0).
"""

def find_ratio_of_lengths(l1, l2):
    # Validate inputs are integers and non-negative
    if not isinstance(l1, int) or not isinstance(l2, int):
        raise TypeError(f"Both arguments must be integers. Received types: {type(l1)}, {type(l2)}")

    # Ensure we don't divide by zero explicitly before simplifying via GCD logic which handles it well
    if l1 < 0 or l2 < 0:
        raise ValueError("Length values should not be negative.")

    from math import gcd
    
    g = abs(gcd(l1, l2))
    
    simplified_l1 = l1 // g
    simplified_l2 = l2 // g
        
    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    pass
