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
        ValueError: If the provided unit is not supported.
    """
    if unit == "meters":
        return float(length)
    elif unit == "feet":
        return length * 0.3048
    elif unit == "kilometers":
        return length * 1000.0
    
    raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    # Sample conversions without interactive input
    print(convert_length(5, 'meters'))      # Output: 5.0
    print(convert_length(20, 'feet'))       # Output: 6.096
    print(convert_length(3, 'kilometers'))  # Output: 3000.0
    
    try:
        convert_length(10, 'yards')         # This should raise ValueError
    except ValueError as e:
        print(f"Error caught: {e}")