def convert_volume(volume: float, source_unit: str, target_unit: str = None) -> dict:
    """
    Converts a volume from one unit to another using predefined conversion rates.
    
    Args:
        volume (float): The volume value to be converted.
        source_unit (str): The source unit of the volume.
        target_unit (str, optional): The target unit for conversion. If None, returns 
                                    a dictionary with both original and potential conversions.

    Returns:
        dict: A dictionary containing the input parameters and the result(s) of the conversion.
              Keys are 'input_volume', 'source_unit', 'target_unit' (if provided), 
              and 'converted_value'. If target_unit is None, includes all possible common targets.

    Raises:
        ValueError: If source or target unit is not recognized.
        TypeError: If input types are incorrect.
    """
    
    # Define conversion rates relative to liters
    base_rates = {
        "liter": 1.0,
        "milliliter": 0.001,
        "kiloliter": 1000.0,
        "gallon (US)": 3.78541,
        "quart (US)": 0.946353,
        "pint (US)": 0.473176,
        "cup (US)": 0.236588,
        "fluid ounce (US)": 0.0295735,
    }

    # Normalize input types and validate existence of units
    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a numeric value.")
    
    source_unit_lower = str(source_unit).strip().lower()
    target_unit_lower = None
    
    if target_unit is not None:
        target_unit_lower = str(target_unit).strip().lower()

    # Check for valid units in base_rates dictionary
    available_units = list(base_rates.keys())
    
    if source_unit_lower not in [u.lower() for u in available_units]:
        raise ValueError(f"Invalid source unit. Available: {', '.join(available_units)}")

if __name__ == '__main__':
    pass
