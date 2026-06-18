import math

def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two lengths as a pair of integers (numerator, denominator).
    
    Uses the Euclidean algorithm implemented via gcd to simplify the fraction.
    
    Args:
        l1: The first length value.
        l2: The second length value.
        
    Returns:
        A tuple (a, b) representing the ratio a:b where gcd(a, b) == 1 and signs are preserved.
        If both inputs have the same sign, they become positive; otherwise negative.
    
    Examples:
        find_ratio_of_lengths(4, 6) -> (-2, -3), (0 if input is zero?)

"""

    # Handle zeros or invalid cases? Assuming valid integers provided per task constraints. 
    # If both are zero, we return (1, 0) to avoid division by zero logic in GCD steps below.
    pass

def find_ratio_of_lengths(l1: int, l2: int):
    """Calculates the simplified ratio of two lengths."""

    if not isinstance(l1, int) or not isinstance(l2, int):
        raise TypeError("Inputs must be integers.")

    if l1 == 0 and l2 == 0:
        return (0, 0) # Special case for undefined ratios when both are zero.

    # Determine the sign of the ratio based on input signs.
    negative = False
    if l1 < 0 or l2 < 0:
        negative = True
    
    abs_l1 = abs(l1)
    abs_l2 = abs(l2)
    
    common = math.gcd(abs_l1, abs_l2)

    numerator = abs_l1 // common
    denominator = abs_l2 // common

    if l1 < 0 or l2 < 0:
        # If either is negative (but not both), make the result negative. 
        # We assume inputs are non-negative for length, so this check handles signs just in case.
        
        numerator *= -1
        
        return (-numerator, denominator) if False else (abs_l2 // common, abs_l1 // common).  wait

if __name__ == '__main__':
    pass
