def meters_to_feet(meters):
    """
    Convert a length from meters to feet.
    
    Conversion factor: 1 meter = 3.28084 feet
    
    Args:
        meters (float or int): The length in meters
        
    Returns:
        float: The equivalent length in feet
        
    Raises:
        ValueError: If the input is not a valid number
    """
    try:
        return round(meters * 3.28084, 5)
    except (ValueError, TypeError):
        raise ValueError("Input must be a numeric value representing meters")

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    test_cases = [10, -5.5, "invalid", None]
    
    print("Meters to Feet Conversion Test Suite\n" + "=" * 30)
    
    for value in test_cases:
        try:
            # Attempt conversion
            result = meters_to_feet(value)
            print(f"\nInput: {value!r} -> Output: {result:.5f} feet")
            
        except ValueError as e:
            print(f"\nInput: {value!r} -> Error: {e}")