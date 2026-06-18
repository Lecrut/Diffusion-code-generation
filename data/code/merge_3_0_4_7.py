def inches_to_cm(inches: float) -> float:
    """
    Convert a length given in inches to centimeters.
    
    The conversion factor is defined as exactly 2.54 cm per inch, which 
    provides the required mathematical precision for this task.
    
    Args:
        inches (float): Length value in inches. Should be non-negative.
        
    Returns:
        float: Equivalent length in centimeters.
    """
    return inches * 2.54

if __name__ == '__main__':
    # Hard-coded sample values for testing the conversion function
    sample_inches = [1, 12, 36]
    
    print("Inches to Centimeters Conversion Results:")
    for inch_val in sample_inches:
        cm_value = inches_to_cm(inch_val)
        print(f"{inch_val} inches is exactly {cm_value} centimeters")