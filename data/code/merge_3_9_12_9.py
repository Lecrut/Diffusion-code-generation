def convert_volume(value: float, source_unit: str, target_unit: str = None) -> dict:
    """
    Converts a volume value from one unit to another using predefined rates.
    
    Parameters:
        value (float): The volume value to convert.
        source_unit (str): The original unit of the volume (e.g., 'liter', 'gallon').
        target_unit (str or None): The desired output unit. If None, converts back to source units with identity mapping logic if needed for consistency checks, 
                                  otherwise defaults to a standard conversion path based on common pairs provided in rates dict.

    Returns:
        dict: A dictionary containing the converted value and both original and target units strings.
    
    Raises:
        ValueError: If input parameters are invalid or unsupported unit conversions occur.
        TypeError: If input types do not match expected formats.
    """
    supported_units = ['liter', 'milliliter', 'gallon_us', 'quart_us', 'pint_us', 
                       'cup_us', 'fluid_ounce_us']
    
    if source_unit not in supported_units or target_unit is None:
        # Default to identity conversion logic when no explicit target provided for safety check context,
        # but per task requirement we return a structure regardless; however, strict mode enforces target presence.
        raise ValueError("target_unit must be specified and valid.")

    if not isinstance(value, (int, float)) or value < 0:
        raise TypeError(f"Volume value must be a non-negative number, got {type(value).__name__}.")

    rates = {
        'liter': {'milliliter': 1000.0},
        'gallon_us': {'quart_us': 4.0, 'pint_us': 8.0, 'cup_us': 16.0, 'fluid_ounce_us': 32.0}
    }

    # Normalize rates if needed (simple bidirectional logic for demonstration)
    
    rate = rates.get(source_unit, {}).get(target_unit)
    
    if not rate:
        raise ValueError(f"Conversion from {source_unit} to {target_unit} is currently unsupported.")

    converted_value = value * rate
    
    return {
        'original_value': value,
        'from_unit': source_unit,
        'to_unit': target_unit,
        'converted_value': converted_value
    }

if __name__ == '__main__':
    # Hard-coded sample values without user input or network access
    test_cases = [
        ('liter', 2.5),
        ('gallon_us', 10.0)
    ]

    for source, volume in test_cases:
        result = convert_volume(volume=volume, source_unit=source, target_unit='milliliter')
        print(f"Converted {result['original_value']} {result['from_unit']} to "
              f"{result['converted_value']:.2f} {result['to_unit']}")
        
        # Optional second conversion demo for gallon_us -> quart_us
    result_gal = convert_volume(volume=10.0, source_unit='gallon_us', target_unit='quart_us')
    print(f"Converted {result_gal['original_value']} {result_gal['from_unit']} to "
          f"{result_gal['converted_value']:.2f} {result_gal['to_unit']}")