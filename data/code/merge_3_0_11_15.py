def convert_length(length: float, unit: str) -> float:
    """
    Converts a length value from meters to feet if input is 'm', 
    or converts from feet to meters if input is 'ft'.
    
    Conversion factors used (standard definitions):
    1 meter = 3.28084 feet
    1 foot = 0.3048 meters
    
    Args:
        length (float): The value to convert.
        unit (str): The source unit ('m' for meters, 'ft' for feet).
        
    Returns:
        float: The converted length in the opposite unit.
    """
    
    # Define conversion constants using standard library precision requirements
    M_TO_FT_FACTOR = 3.28084
    FT_TO_M_FACTOR = 0.3048
    
    if unit == 'm':
        return length * M_TO_FT_FACTOR
    elif unit == 'ft':
        return length * FT_TO_M_FACTOR
    else:
        raise ValueError(f"Unsupported unit '{unit}'. Use 'm' or 'ft'.")

if __name__ == '__main__':
    # Hard-coded sample values for testing the function
    
    # Sample 1: Convert 5 meters to feet
    result_m_to_ft = convert_length(5.0, 'm')
    
    # Sample 2: Convert 10 feet to meters
    result_ft_to_m = convert_length(10.0, 'ft')
    
    print(f"Converted {result_m_to_ft:.4f} ft from 5 m")
    print(f"Converted {result_ft_to_m:.4f} m from 10 ft")