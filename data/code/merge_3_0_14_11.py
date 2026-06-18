def convert_length(length, unit):
    """
    Converts a numerical length to meters based on the target unit string.
    
    Supported units: 'meters', 'feet', 'kilometers'.
    
    Args:
        length (float or int): The numerical value of the length.
        unit (str): The target unit for conversion ('meters', 'feet', 'kilometers').
        
    Returns:
        float: The converted length in meters.
        
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    
    # Define supported units and their conversion factors to meters
    supported_units = {
        "meters": 1,
        "feet": 0.3048,
        "kilometers": 1000
    }

    if unit not in supported_units:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are 'meters', 'feet', and 'kilometers'.")

    return length * supported_units[unit]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test 1: Convert 5 feet to meters
    result_feet = convert_length(5, "feet")
    
    # Test 2: Convert 0.5 kilometers to meters
    result_km = convert_length(0.5, "kilometers")
    
    # Test 3: Convert 100 meters to meters (identity check)
    result_meters = convert_length(100, "meters")
    
    print(f"5 feet is {result_feet} meters.")
    print(f"0.5 kilometers is {result_km} meters.")
    print(f"100 meters is {result_meters} meters.")

    # Test 4: Demonstrate ValueError for unsupported unit
    try:
        convert_length(10, "yards")
    except ValueError as e:
        print(f"Caught expected error: {e}")