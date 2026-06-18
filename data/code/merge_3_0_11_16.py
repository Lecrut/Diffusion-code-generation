def convert_length(length: float, unit_type: str) -> float:
    """
    Converts a length value from meters to feet or vice versa.
    
    Conversion factors used (approximate):
    1 meter = 3.28084 feet
    
    Args:
        length: The numerical value of the length.
        unit_type: A string indicating 'm' for meters or 'ft' for feet.
        
    Returns:
        The converted length as a float.
    """
    
    # Define conversion factor from meters to feet
    METERS_TO_FEET = 3.28084
    
    if unit_type == 'm':
        return length * METERS_TO_FEET
    elif unit_type == 'ft':
        return length / METERS_TO_FEET
    else:
        raise ValueError(f"Unsupported unit type '{unit_type}'. Use 'm' or 'ft'.")

if __name__ == '__main__':
    # Hard-coded sample values for testing the function
    
    # Convert 10 meters to feet
    result_m_to_ft = convert_length(10, 'm')
    
    # Convert 32.8 feet back to meters (should be approximately 10)
    result_ft_to_m = convert_length(result_m_to_ft, 'ft')
    
    print(f"Converted {result_m_to_ft:.4f} ft")
    print(f"Rounded: {int(round(result_ft_to_m))}")