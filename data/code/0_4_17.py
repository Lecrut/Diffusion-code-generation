def inches_to_centimeters(inches: float) -> float:
    """
    Convert a length given in inches to centimeters using the precise conversion factor.
    
    1 inch = exactly 2.54 cm by international definition.
    
    Args:
        inches (float): The length value in inches. Must be non-negative or positive as required.
        
    Returns:
        float: The equivalent length in centimeters.
        
    Example:
        >>> inches_to_centimeters(1)
        2.54
        >>> inches_to_centimeters(72)
        182.88
    """
    return inches * 2.54

if __name__ == '__main__':
    # Hard-coded sample values for testing the conversion function
    test_cases = [0, 1, 12, 36, 72]
    
    print("Inches to Centimeters Conversion Results:")
    for inches_value in test_cases:
        cm_result = inches_to_centimeters(inches_value)
        # Using formatted strings for precise output based on the mathematical precision of float operations with finite decimal inputs like 2.54
        print(f"{inches_value} inches is {cm_result:.6f} centimeters")