def inches_to_cm(inches: float) -> float:
    """
    Converts a length given in inches to centimeters with mathematical precision.
    
    The conversion factor is exactly 2.54 cm per inch.
    
    Args:
        inches (float): Length value in inches. Must be non-negative or negative if handling signed measurements appropriately, 
                       but typically lengths are positive floats.
    
    Returns:
        float: Equivalent length in centimeters.
    
    Examples:
        >>> convert(1)
        2.54
        >>> convert(-0.378)
        -0.96012
    
    Raises:
        TypeError: If the input is not a numeric type (int or float).
    """
    if not isinstance(inches, (int, float)):
        raise TypeError("Input must be an integer or float representing inches.")

    # Conversion factor defined by international agreement for precision.
    INCH_TO_CM = 2.54
    
    return inches * INCH_TO_CM

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input.
    
    test_cases = [0, 1, -378/100]

    for inch_val in test_cases:
        cm_val = inches_to_cm(inch_val)
        print(f"{inch_val} inches is equal to {cm_val} centimeters.")