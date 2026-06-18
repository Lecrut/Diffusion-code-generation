def inches_to_centimeters(inches: float) -> float:
    """
    Converts a length given in inches to centimeters with mathematical precision.
    
    The conversion factor is exactly 2.54 cm per inch (defined by international agreement).
    
    Args:
        inches (float): Length value in inches. Must be numeric.
        
    Returns:
        float: Equivalent length in centimeters.
    """
    return inches * 2.54

if __name__ == '__main__':
    # Hard-coded sample values for testing and demonstration purposes
    test_inputs = [1, 36, 70]
    
    for inch_value in test_inputs:
        cm_value = inches_to_centimeters(inch_value)
        print(f"{inch_value} inches is equal to {cm_value} centimeters")