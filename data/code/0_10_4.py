def meters_to_feet(meters: float) -> float:
    """
    Converts a length given in meters to feet.
    
    Conversion factor: 1 meter = 3.28084 feet
    
    Args:
        meters (float): The length in meters.
        
    Returns:
        float: The equivalent length in feet.
    """
    if not isinstance(meters, (int, float)):
        raise TypeError("Input must be a numeric value.")
    
    return meters * 3.28084

if __name__ == '__main__':
    # Sample test cases without interactive input
    
    try:
        sample_meters = [10.5, -2.0, 0]
        
        for val in sample_meters:
            feet_value = meters_to_feet(val)
            print(f"{val} meters is equal to {feet_value:.4f} feet")
            
    except Exception as e:
        print(f"An error occurred during processing: {e}")