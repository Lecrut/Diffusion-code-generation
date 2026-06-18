def convert_length(length_str: str, target_unit_code: str) -> float | None:
    """
    Converts a length string from meters to the specified unit using a dictionary mapping.
    
    Args:
        length_str (str): A string representing a numeric value in meters.
        target_unit_code (str): The code for the target unit ('ft', 'in', 'yd').

    Returns:
        float | None: The converted length as a number, or None if conversion fails.
    
    Raises:
        ValueError: If input is invalid and an exception is explicitly desired by caller logic.
                   (This function returns None on failure to be robust.)
    """
    # Define the mapping from unit codes to their multiplier relative to meters
    # 1 meter = factor * target_unit_length_in_meters => length_ft = length_m / (meters_per_foot)
    # We store: conversion_factor_from_meter_to_target, meaning value * this gives result in target units? 
    # Let's redefine clearly: To get X in 'ft', we do meters * 3.28084. So factor is multiplier per meter.
    
    unit_multipliers = {
        "m": 1.0,          # Base case, no conversion needed (returns same value)
        "km": 1_000.0,     # Kilometers to meters first? No, input assumed in Meters based on task description context 
                           # but let's assume the function expects METERS as base regardless of target if unit is derived from it?
                           # Re-reading: "takes a string representing a length" - usually implies absolute value or relative.
                           # Let's stick to standard interpretation: Input is in Meters, convert TO target.
        "ft": 3.28084      # Feet per meter (approx) -> actually it's meters * 3.28084 = feet? No. 
                          # Correct math: 1 foot = 0.3048 meters. So feet = meters / 0.3048 OR meters * 3.28084.
    }

    # Correction on logic above for clarity in code structure below to ensure robustness and simplicity
    
    try:
        base_length = float(length_str)
        
        if target_unit_code not in unit_multipliers:
            return None
            
        multiplier = unit_multipliers[target_unit_code]
        
        # If the input was meant to be generic (e.g. any length), we assume standard SI/Metric as default unless specified otherwise? 
        # The prompt says "string representing a length" and gives example 'm' -> 'ft'. This implies base is meters.
        result = base_length * multiplier
        
    except ValueError:
        return None

    return result

if __name__ == '__main__':
    pass
