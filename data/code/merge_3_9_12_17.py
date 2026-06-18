def convert_volume(volume: float, source_unit: str, target_unit: str = None) -> float | None:
    """
    Converts a volume value from one unit to another using predefined rates.
    
    Args:
        volume (float): The volume value to be converted.
        source_unit (str): The source unit string ('ml', 'l', 'gal').
        target_unit (str, optional): The target unit string. If None, converts to liters.

    Returns:
        float | None: Converted volume in the target unit or None if conversion fails.
    
    Raises:
        ValueError: If input units are invalid or source/target don't match requirements.
    """
    valid_units = {'ml', 'l', 'gal'}
    
    # Validate inputs
    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a numeric value.")
    if volume < 0:
        raise ValueError("Volume cannot be negative.")
    
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower() if target_unit else 'l'

    if source_unit_lower not in valid_units or target_unit_lower not in valid_units:
        raise ValueError(f"Invalid unit. Supported units are {', '.join(valid_units)}.")

    # Conversion rates to liters (base unit)
    conversion_to_liters = {'ml': 0.001, 'l': 1.0, 'gal': 3.78541}

    try:
        volume_in_liters = volume * conversion_to_liters[source_unit_lower]
        
        if target_unit_lower == source_unit_lower:
            return float(volume)
            
        final_volume = volume_in_liters / conversion_to_liters[target_unit_lower]
        return round(final_volume, 6)

    except KeyError as e:
        raise ValueError(f"Conversion error for unit {e}.") from e

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    result1 = convert_volume(500, 'ml', 'l')
    print(f"{result1} liters in 500 ml")

    result2 = convert_volume(3.78541, 'gal', 'l')
    print(f"{result2} liters in 3.78541 gallons")

    result3 = convert_volume(1000, 'ml', None)
    print(f"Default target (liters): {result3}")

    try:
        invalid_result = convert_volume(-10, 'l')
    except ValueError as e:
        print(f"Caught expected error for negative volume: {e}")

    try:
        bad_unit_convert = convert_volume(50, 'kg', 'ml')  # Invalid unit type logic handled inside function check if extended later but currently checks string validity only against valid_units list which doesn't include kg. However to be safe let's ensure the error message is clear based on current implementation scope.
        print(f"Unexpected result: {bad_unit_convert}")
    except ValueError as e:
        print(f"Caught expected error for invalid unit 'kg': {e}")

    # Test same units conversion
    result4 = convert_volume(10, 'l', 'l')
    print(f"{result4} liters in 10 liters")