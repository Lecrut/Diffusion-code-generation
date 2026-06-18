import math

def inches_to_centimeters(inches: float) -> float:
    """
    Convert a length given in inches to centimeters with mathematical precision.
    
    Conversion factor is exactly 2.54 cm per inch (defined by international standard).
    
    Args:
        inches (float): Length value in inches. Must be non-negative for physical lengths, 
                       though the function does not enforce this constraint strictly as it performs pure conversion.
        
    Returns:
        float: Equivalent length in centimeters.
    """
    return inches * 2.54

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_cases = [3, 12, 28.3479]
    
    print("Inches to Centimeters Conversion Results:")
    for inch_val in test_cases:
        cm_value = inches_to_centimeters(inch_val)
        # Print with sufficient precision; using repr ensures no rounding errors are hidden
        print(f"{inch_val} inches = {cm_value:.6f} centimeters")