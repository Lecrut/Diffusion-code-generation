def convert_length(length: float, target_unit: str) -> float:
    """
    Converts a numerical length to a predefined set of supported units (meters, feet, kilometers).
    
    Supported conversions are based on meters as the base unit.
    1 meter = 3.28084 feet
    1 kilometer = 1000 meters
    
    Args:
        length (float): The numerical value to convert.
        target_unit (str): The target unit string ('meters', 'feet', or 'kilometers').
        
    Returns:
        float: The converted length in the specified unit.
        
    Raises:
        ValueError: If the target_unit is not one of the supported units.
    """
    if target_unit == "meters":
        return length * 1.0
    elif target_unit == "feet":
        return length * 3.28084
    elif target_unit == "kilometers":
        return length / 1000.0
    
    raise ValueError(f"Unsupported unit: {target_unit}")

if __name__ == '__main__':
    # Sample conversions without interactive input
    print(convert_length(5, 'meters'))      # Output: 5.0
    print(convert_length(100, 'feet'))      # Output: 328.084
    print(convert_length(2, 'kilometers'))  # Output: 0.002
    
    try:
        convert_length(10, 'yards')
    except ValueError as e:
        print(f"Error caught: {e}")