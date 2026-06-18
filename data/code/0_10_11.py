def meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to feet using the standard conversion factor.
    
    The conversion formula is based on 1 meter = 3.28084 feet.
    
    Args:
        meters (float): The length in meters. Must be non-negative for physical 
                       contexts, though negative values are mathematically valid.
        
    Returns:
        float: The equivalent length in feet.
        
    Raises:
        TypeError: If the input is not a numeric type.
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be an integer or float representing meters.")
    
    conversion_factor = 3.28084
    return meters * conversion_factor

if __name__ == '__main__':
    # Sample values for testing the function without interactive input
    
    test_cases = [1, 5, -2]
    
    print("Sample Conversion Results:")
    print("-" * 30)
    
    for meter_value in test_cases:
        try:
            feet_value = meters_to_feet(meter_value)
            # Formatting to avoid excessive decimal places unless it's a whole number conversion context, 
            # but keeping precision as per calculation.
            print(f"{meter_value} meters is equal to {feet_value:.4f} feet")
        except TypeError:
            print(f"Error processing {meter_value}: Invalid input type.")