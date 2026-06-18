def convert_volume(volume: float, source_unit: str, target_unit: str = None) -> float:
    """
    Converts a volume value from one unit to another using predefined rates.
    
    Args:
        volume (float): The volume value to be converted.
        source_unit (str): The unit of the input volume (e.g., 'ml', 'l', 'gal').
        target_unit (str, optional): The desired output unit. If None, returns 
                                    a default conversion based on context or raises error if both are same.

    Returns:
        float: Converted volume value in the target unit.

    Raises:
        ValueError: If units are invalid, source equals target without explicit handling,
                   or input is not numeric.
    """
    
    # Define supported units and their conversion factors relative to liters (1 L = 1000 ml)
    UNIT_FACTORS_TO_LITERS = {
        'ml': 0.001,      # milliliters per liter
        'l': 1.0,         # liters per liter
        'cl': 0.01,       # centiliters per liter
        'dl': 0.1,        # deciliters per liter
        'gal': 3.78541,   # gallons per liter (US)
    }

    def validate_and_normalize(value: float, unit_str: str):
        """Validates input and returns normalized value in liters."""
        if not isinstance(value, (int, float)):
            raise ValueError(f"Volume must be a numeric type, got {type(value).__name__}")
        
        valid_units = set(UNIT_FACTORS_TO_LITERS.keys())
        unit_str_lower = str(unit_str).lower().strip()
        if unit_str_lower not in valid_units:
            raise ValueError(f"Unsupported volume unit '{unit_str}'. Supported units are {', '.join(valid_units)}")
        
        return value * UNIT_FACTORS_TO_LITERS[unit_str_lower]

    # Validate inputs
    try:
        source_liters = validate_and_normalize(volume, source_unit)
    except (ValueError, TypeError):
        raise ValueError("Invalid input for volume or source unit.") from None

    if target_unit is None:
        # Default behavior: return value in liters unless explicitly told otherwise? 
        # Or perhaps assume same as source? Let's default to Liters.
        pass
    
    try:
        target_liters = validate_and_normalize(volume, target_unit)
    except (ValueError, TypeError):
        raise ValueError("Invalid input for volume or target unit.") from None

    if not isinstance(target_unit, str):
        raise ValueError(f"Target unit must be a string, got {type(target_unit).__name__}")

    # If no target provided, we can't guess the user's intent perfectly without more context. 
    # However, to avoid returning just liters when they might want ml or gal back:
    if target_unit is None and source_liters == volume * 1.0:
        raise ValueError("Target unit must be specified.")

    # Calculate conversion factor between source and target directly
    factor = UNIT_FACTORS_TO_LITERS.get(target_unit.lower()) / UNIT_FACTORS_TO_LITERS[source_unit.lower()]
    
    if not isinstance(factor, float):
        raise ValueError(f"Conversion failed: Invalid units '{source_unit}' to '{target_unit}'.")

    return source_liters * factor

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies
    
    test_cases = [
        {
            'input_volume': 50, 
            'source_unit': 'ml', 
            'target_unit': 'l'
        },
        {
            'input_volume': 2.5, 
            'source_unit': 'gal', 
            'target_unit': 'l'
        },
        {
            'input_volume': 100, 
            'source_unit': 'cl', 
            'target_unit': None # Should default to liters based on logic above or raise error if strict
        }
    ]

    print("Running sample conversions...")
    
    for i, case in enumerate(test_cases):
        vol = case['input_volume']
        src = case['source_unit']
        
        try:
            # Handle None target by forcing 'l' as default fallback if needed 
            # but per spec we need to handle gracefully. Let's assume explicit is better or raise.
            # To ensure it runs without error, let's set a safe default for the last case in this demo context
            tgt = case.get('target_unit', 'l') 
            
            result = convert_volume(vol, src, tgt)
            
            print(f"Test Case {i+1}:")
            print(f"  Input: {vol} {src}")
            if tgt is not None:
                print(f"  Output ({tgt}): {result:.4f}")
            else:
                # Fallback logic for demo purposes since spec says handle gracefully 
                # and we can't guess user intent perfectly without a default rule.
                result = convert_volume(vol, src) if tgt is None else convert_volume(vol, src, 'l')
                
        except ValueError as e:
            print(f"Test Case {i+1}: Error - {e}")

    # Additional error handling test case
    try:
        invalid_result = convert_volume(50, "invalid_unit", "gal")
    except ValueError as ve:
        print("Error Handling Test:")
        print(f"  Caught expected error for 'invalid_unit': {ve}")