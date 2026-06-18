def calculate_length_ratio(length1: float, length2: float) -> float:
    """
    Calculates the ratio of two floating-point numbers accurately 
    within standard IEEE 754 double-precision limits.

    Parameters:
        length1 (float): The numerator in the ratio calculation.
        length2 (float): The denominator in the ratio calculation.

    Returns:
        float: The result of dividing length1 by length2, rounded 
              to avoid minor floating-point representation discrepancies 
              for common simple fractions where appropriate using a small epsilon check logic if needed,
              but primarily relying on Python's native double precision division which is already optimized and accurate within standard limits.

    Raises:
        ZeroDivisionError: If length2 is zero or extremely close to it (considered effectively zero).
    """
    
    # Define an effective tolerance for "zero" based on typical float noise, 
    # though Python's native division handles most edge cases well unless denormalized numbers are involved.
    EPSILON = 1e-9

    if abs(length2) < EPSILON:
        raise ZeroDivisionError("Length2 is too close to zero; ratio calculation undefined.")
    
    result = length1 / length2
    
    # Optional refinement: For very small integers represented as floats, 
    # standard division might yield 0.999999 or 1.000001 due to binary representation imprecision.
    # While "accurate to the limits of standard floating-point arithmetic" usually means we trust native float behavior,
    # some contexts prefer snapping obvious fractions (like 4/2=2) for display cleanliness without changing logic.
    # Given the strict instruction "limits of standard", we will NOT round arbitrarily but ensure no custom 
    # non-standard rounding modes interfere with Python's optimal C-level division.

    return result

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    
    s1 = 4.0
    s2 = 3.5
    
    ratio_result = calculate_length_ratio(s1, s2)
    
    print(f"Ratio of {s1} and {s2}:")
    print(ratio_result)