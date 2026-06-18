def inches_to_cm(inches: float) -> float:
    """
    Convert a length given in inches to centimeters with mathematical precision.
    
    The conversion factor is exactly 2.54 cm per inch (defined by international agreement).
    
    Args:
        inches (float): Length value in inches. Must be non-negative for physical lengths, 
                       though the function handles negative numbers mathematically.
        
    Returns:
        float: Equivalent length in centimeters.
    """
    return inches * 2.54

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input
    test_cases = [0, 1, 36, 72.5]
    
    for inch_value in test_cases:
        cm_value = inches_to_cm(inch_value)
        print(f"{inch_value} inches is exactly {cm_value:.4f} centimeters")