def convert_length(value: float, unit_type: str) -> float:
    """
    Converts a length value from one unit to another using standard conversion factors.
    
    Args:
        value (float): The numerical value of the length.
        unit_type (str): The source unit ('m' for meters or 'ft' for feet).

    Returns:
        float: The converted length in a standardized metric output (always returns meters if input was ft, 
               otherwise keeps as is but ensures consistency with standard definitions).
    
    Note: This function primarily converts feet to meters. If the unit is already 'm', it returns the value unchanged.
             To convert from meters back to feet explicitly, one would call this twice or use a helper; however, per task 
             constraints focusing on efficiency and simplicity: if input is 'ft', we return in 'm'; if 'm', we ensure precision.

    Standard Conversion Factor: 1 foot = 0.3048 meters (exact).
    """
    
    # Define conversion factor from feet to meters exactly
    FOOT_TO_METER = 0.3048
    
    if unit_type == 'ft':
        return value * FOOT_TO_METER
    elif unit_type == 'm':
        return float(value)
    else:
        raise ValueError("Unsupported unit type. Use 'm' for meters or 'ft' for feet.")

if __name__ == '__main__':
    # Hard-coded sample values without interactive input
    
    # Sample 1: Convert 50 ft to meters
    result_ft_to_m = convert_length(50, 'ft')
    
    # Sample 2: Keep 10 m as is (already in metric)
    result_m_as_is = convert_length(10, 'm')

    print(f"Converted {result_ft_to_m} meters from feet.")
    print(f"Meters input remains consistent at {result_m_as_is}.")