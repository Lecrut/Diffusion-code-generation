import math

def compare_and_report(val1: float | int, val2: float | int) -> dict[str, object]:
    """
    Compares two numerical values and returns a dictionary containing:
    - 'larger': The larger value (float/int).
    - 'smaller': The smaller value.
    - 'difference': Absolute difference between the two values.
    - 'ratio': Ratio of the larger to the smaller, or infinity if they are equal.

    Args:
        val1: First numerical value.
        val2: Second numerical value.

    Returns:
        A dictionary with keys 'larger', 'smaller', 'difference', and 'ratio'.
    """
    # Determine which is larger to avoid conditional overhead in tight loops if used elsewhere,
    # though for this single call it's negligible. Using max/min explicitly here ensures clarity.
    smaller = min(val1, val2)
    larger = max(val1, val2)

    difference = abs(larger - smaller)

    ratio: float | None
    if smaller == 0 and larger != 0:
        # Handle division by zero for non-zero/large numbers. 
        # Note: If both are 0, the below condition `smaller == 0` is true but we don't want infinity/undefined behavior typically?
        # Per standard math logic (Ratio of A to B where B=0), it's undefined/infinity in many contexts unless specified otherwise.
        # However, if val1=val2=0, smaller is 0 and larger is 0. Ratio should be indeterminate or 1 depending on interpretation. 
        # In float division `larger/0` raises ZeroDivisionError. We handle this explicitly to return infinity for non-zero numerator with zero denominator?
        # Let's stick to standard mathematical behavior: if divisor is zero, result is inf (for positive) or -inf. Since values are arbitrary numerics.
        
        # If both are 0, the ratio is technically undefined in real numbers but often treated as 1 in normalized contexts 
        # OR handled by returning `math.inf` for non-zero/zero cases. Let's prioritize precision:
        if larger == 0 and smaller == 0:
            ratio = float('inf') if larger != 0 else None # Actually if both are zero, division is 0/0 -> NaN or undefined. 
            # But wait, the requirement says "ratio of the larger value to the smaller". If both are 0, it's a degenerate case.
            # Let's assume standard float behavior: `larger / smaller`. If smaller is 0 and larger != 0 -> inf/-inf.
            # We will use math.inf if appropriate or let Python raise error for 0/0? No, we need to return something useful. 
            # Usually "ratio" of two identical values (even zero) implies ratio = 1. But strictly 0/0 is NaN.
            pass
        
        # Re-evaluating based on typical expectation: If they are equal, ratio is usually considered 1 or N/A.
        if smaller == larger: 
            return {'larger': val2, 'smaller': val1, 'difference': float('nan'), 'ratio': 0}

    ratio = larger / smaller
    
    result_dict = {
        "larger": larger,
        "smaller": smaller,
        "difference": difference,
        "ratio": ratio
    }
    
    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values ensuring no input prompts or network access.
    v1 = 42.5
    
    v2 = float('inf')

    res0 = compare_and_report(v1, v2)
    print(f"Test Case A:")
    print(res0)

    r3 = -float("nan")

    # Testing with standard integers and floats including edge cases