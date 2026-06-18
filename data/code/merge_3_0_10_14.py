def meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to feet using the standard conversion factor (1 meter = 3.28084 feet).
    
    Args:
        meters (float): The length value in meters. Must be a numeric type.
        
    Returns:
        float: The equivalent length in feet, rounded to two decimal places for readability.
        
    Raises:
        TypeError: If the input is not an instance of int or float.
        ValueError: If the input contains non-numeric characters when converted via try-except logic (though 
                   this function assumes valid numeric types based on type checking).
    """
    
    # Define conversion factor
    FEET_PER_METER = 3.28084
    
    # Validate input type to ensure it is a number before calculation
    if not isinstance(meters, (int, float)):
        raise TypeError(f"Expected numeric value for meters, got {type(meters).__name__}")
    
    # Perform conversion and round the result
    feet = meters * FEET_PER_METER
    
    return round(feet, 2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without interactive input
    test_cases = [1.0, 5.6789, -3.4]

    for meters in test_cases:
        try:
            feet_value = meters_to_feet(meters)
            print(f"{meters} meters is equal to {feet_value} feet.")
        except (TypeError, ValueError) as e:
            # Gracefully handle any unexpected errors during conversion or validation
            print(f"Error processing input '{meters}': {e}")