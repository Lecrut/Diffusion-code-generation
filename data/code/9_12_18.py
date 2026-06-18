def convert_volume(volume: float, source_unit: str, target_unit: str = None) -> float:
    """
    Converts a volume value from one unit to another using predefined rates.
    
    Args:
        volume (float): The volume value to convert.
        source_unit (str): The current unit of the volume ('ml', 'l', 'gal', 'qt').
        target_unit (str, optional): The desired unit for conversion. If None, 
                                    converts back to original units or defaults based on context logic.

    Returns:
        float: Converted volume value in the specified or default unit.
    
    Raises:
        ValueError: If input values are invalid or unsupported units are provided.
    """
    # Define base conversion rates relative to liters (1 liter = 1000 ml)
    rate_to_liter = {
        'ml': 0.001,       # milliliters to liters
        'l': 1.0,          # liters to liters
        'gal': 3.785411784, # gallons (US) to liters
        'qt': 0.946352946   # quarts (US) to liters
    }

    valid_units = set(rate_to_liter.keys())
    
    if source_unit not in valid_units:
        raise ValueError(f"Unsupported source unit '{source_unit}'. Valid units are {', '.join(valid_units)}")
    
    target_unit_normalized = target_unit.lower() if isinstance(target_unit, str) else None
    
    # If no target unit is specified and we have a default behavior requirement (e.g., return to input scale or specific base), 
    # but since the prompt implies explicit conversion logic, we will enforce that target_unit must be provided unless it's same as source.
    if not target_unit_normalized:
        raise ValueError("Target unit must be specified.")

    if target_unit_normalized not in valid_units:
        raise ValueError(f"Unsupported target unit '{target_unit}'. Valid units are {', '.join(valid_units)}")

    # Convert to base (liters) first, then to target
    try:
        volume_float = float(volume)
        
        intermediate_liters = volume_float * rate_to_liter[source_unit]
        converted_value = intermediate_liters / rate_to_liter[target_unit_normalized]
        
        return round(converted_value, 6)

    except (ValueError, TypeError):
        raise ValueError("Volume must be a valid numeric value.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per requirements
    
    sample_1 = convert_volume(500, "ml", "l")
    
    sample_2 = convert_volume(3.785411784 * 10, "gal", "qt")
    
    print(f"Sample 1: {sample_1}")
    # Expected output for Sample 1: 0.5
    
    try:
        invalid_unit_test = convert_volume(100, "kg") 
    except ValueError as e:
        print(f"Error caught (expected): {e}")

    sample_3 = convert_volume(4, "qt", None) # This should raise an error based on logic above if strict target required.
    
    try:
        result_sample_3 = convert_volume(4, "qt") 
    except ValueError as e:
        print(f"Error caught for missing target (expected): {e}")

    sample_4 = convert_volume("invalid", "l", "ml") # Non-numeric input
    
    try:
        invalid_num_test = convert_volume("abc", "l", "ml") 
    except ValueError as e:
        print(f"Error caught for non-numeric volume (expected): {e}")

    sample_5 = convert_volume(2, "gal", "qt") # Correct usage
    
    print(f"Sample 4 Result: {sample_5}")