def inches_to_cm(inches: float) -> float:
    """
    Convert a length given in inches to centimeters with mathematical precision.
    
    The conversion factor is exactly 2.54 cm per inch (defined by international standard).
    
    Args:
        inches (float): The length value in inches.
        
    Returns:
        float: The equivalent length in centimeters.
    """
    return inches * 2.54

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    test_values = [1, 36, 70.87]
    
    print("Inches to Centimeters Conversion Results:")
    for val in test_values:
        result = inches_to_cm(val)
        print(f"{val} inch(es) is equal to {result:.2f} cm")