def convert_volume(value: float, source_unit: str, target_unit: str = None) -> float | None:
    """
    Converts a volume value from one unit to another (optional).
    
    Parameters:
        value (float): The volume value to be converted.
        source_unit (str): The initial unit of the volume.
        target_unit (str, optional): The desired output unit. If None, returns original value in source units.

    Returns:
        float or None: Converted volume in target units if successful, otherwise None.

    Supported Units and Base Conversion Factor to Liters:
        milliliter -> 0.001
        liter -> 1.0
        gallon (US) -> 3.78541
        quart (US) -> 0.946353
        pint (US) -> 0.473176
    """

    units_to_liters = {
        "milliliter": 0.001,
        "liter": 1.0,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
    }

    if value is None:
        return None
    
    source_lower = source_unit.lower()
    
    # Check for valid input units
    if source_lower not in units_to_liters and target_unit is None:
        raise ValueError("Input error: Invalid source unit provided.")
    elif target_unit is not None:
        target_lower = target_unit.lower()
        if target_lower not in units_to_liters:
            return None
        
        # Check consistency of input (same value, different inputs)
        try:
            base_liters = float(value) * units_to_liters[source_lower]
            result = base_liters / units_to_liters[target_lower]
            
            if target_unit is not None and source_unit == target_unit:
                return float(result) # Return original value as converted
        
        except (ValueError, TypeError):
            raise ValueError("Input error: Value must be a valid number.")

if __name__ == '__main__':
    pass
