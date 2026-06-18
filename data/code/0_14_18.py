def convert_length(length: float, unit_str: str) -> float:
    """
    Converts a numerical length to meters based on the target unit string.
    
    Supported units (case-insensitive): 'meters', 'feet', 'kilometers'.
    
    Args:
        length (float): The numerical value of the length.
        unit_str (str): The target unit as a string ('meters', 'feet', or 'kilometers').
        
    Returns:
        float: The converted length in meters.
        
    Raises:
        ValueError: If the provided unit is not supported.
    """
    # Define conversion factors to meters and normalize input case
    conversions = {
        "meters": 1,
        "feet": 0.3048,
        "kilometers": 1000
    }

    normalized_unit = unit_str.lower()

    if normalized_unit not in conversions:
        raise ValueError(f"Unsupported unit: {unit_str}. Supported units are meters, feet, kilometers.")

    return length * conversions[normalized_unit]

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no interactive input)
    
    # Test case 1: Convert 50 feet to meters
    result_feet = convert_length(50, "feet")
    print(f"50 feet is {result_feet} meters.")

    # Test case 2: Convert 2 kilometers to meters
    result_km = convert_length(2.5, "kilometers")
    print(f"2.5 kilometers is {result_km} meters.")

    # Test case 3: Convert 100 meters to meters (identity check)
    result_meters = convert_length(100, "meters")
    print(f"100 meters is {result_meters} meters.")

    # Uncomment the line below if you want to test error handling manually during execution.
    # try:
    #     convert_length(50, "yards")  # Should raise ValueError
    # except ValueError as e:
    #     print(f"Error caught: {e}")