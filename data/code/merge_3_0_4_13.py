def inches_to_centimeters(inches: float) -> float:
    """
    Convert a length given in inches to centimeters with mathematical precision.
    
    Conversion factor is exactly 2.54 cm per inch (defined by international standard).
    
    Args:
        inches (float): Length value in inches. Should be non-negative for physical lengths, 
                       though the function will return negative results if input is negative.
    
    Returns:
        float: Equivalent length in centimeters.
    """
    conversion_factor = 2.54
    return inches * conversion_factor

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    test_cases = [0, 1, 6, 12, 36]
    
    print("Inches to Centimeters Conversion:\n")
    for inches in test_cases:
        cm_value = inches_to_centimeters(inches)
        print(f"{inches} inch(es) = {cm_value:.4f} centimeter(s)")