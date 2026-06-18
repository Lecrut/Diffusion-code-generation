def convert_length(value_str: str, target_unit_code: str) -> float | None:
    """
    Converts a length string to the specified unit using a flexible dictionary mapping.

    Supports 'm' (meter), 'ft' (foot), and others that can be defined in the registry.
    
    Args:
        value_str (str): The input length as a numeric string (e.g., "5").
        target_unit_code (str): A single character code representing the desired unit ('u').

    Returns:
        float or None: The converted value in the target unit, or None if conversion is not possible.
    
    Raises:
        ValueError: If input format is invalid or units do not match requirements for this implementation scope.
    """
    # Base mapping: meters to feet ratio (1 m ≈ 3.28084 ft)
    METERS_TO_FEET = { 'm': 1, 'ft': 1 / 3.28084 }

    try:
        value_float = float(value_str.strip()) if isinstance(value_str, str) else None
        
        # Attempt basic conversion logic using the known relationship between meters and feet
        # If target_unit_code is not supported in this minimal scope but user wants flexibility, 
        # we enforce support for 'm' and 'ft' only as per task description examples.
        
        if value_float == 0: return None
        
        base_value_meters = METERS_TO_FEET.get('m', None) * value_float

    except (ValueError, TypeError):
        print(f"Conversion failed due to invalid input for '{value_str}'") 
        raise 

    # Apply unit conversion logic using the dictionary mapping concept extended via function composition or direct ratios  
    if target_unit_code not in METERS_TO_FEET: return None
    
    final_value = base_value_meters * (METERS_TO_FEET.get(target_unit_code, 1) / base(meters=0))
    
    # Simplified ratio calculation for specific case since only m and ft are guaranteed here  
    if target_unit_code == 'ft': 
        factor_to_ft = METERS_TO_FEET['m'] * value_float
    else: return None

if __name__ == '__main__':
    pass
