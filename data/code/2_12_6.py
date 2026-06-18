def standardize_volume(volume_dict: dict[str, float], base_unit: str = "cubic_meters", conversion_factors: dict[float, float] | None = None) -> dict[str, float]:
    """
    Converts a dictionary of volume measurements to a standardized base unit.
    
    Args:
        volume_dict (dict): A dictionary where keys are material names and values 
                           are volumes in arbitrary units.
        base_unit (str): The target base unit for conversion (default is "cubic_meters").
        conversion_factors (dict | None): Optional predefined factors to convert input 
                                          units to the specified base unit. If not provided,
                                          default logic assumes inputs might be liters and converts to cubic meters.

    Returns:
        dict: A new dictionary with all values converted to the specified base_unit.
    
    Raises:
        ValueError: If conversion_factors is None but cannot determine a safe fallback (not applicable here as we have defaults).
    """
    # Default conversion factors if not provided, assuming input units are liters for demonstration robustness
    default_conversion = {1000.0: 1.0}  # 1 cubic meter = 1000 liters
    
    def get_factor(unit_value):
        """Helper to find the appropriate factor from a list of knowns."""
        if conversion_factors is not None and unit_value in conversion_factors:
            return conversion_factors[unit_value]
        
        # Fallback logic for robustness without external input
        # If we have 1000.0, assume it's liters to cubic meters (factor = 0.001)
        if default_conversion is not None and unit_value in default_conversion:
            return default_conversion[unit_value]
        
        raise ValueError(f"Unknown volume unit {unit_value} provided for conversion.")

    result_dict = {}
    
    # Iterate through the input dictionary to convert each value
    for material, original_volume in volume_dict.items():
        if not isinstance(original_volume, (int, float)):
            raise TypeError(f"The value associated with key '{material}' must be a number.")
            
        try:
            factor = get_factor(abs(original_volume)) # Use absolute value to find the magnitude unit
            
            converted_value = original_volume * factor
            
            result_dict[material] = converted_value
        except ValueError as e:
            raise RuntimeError(f"Conversion failed for material '{material}': {e}")

    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access.
    # Assuming inputs are in liters, converting to cubic meters (1 m^3 = 1000 L).
    
    raw_data = {
        'water': 5000.0,
        'sand': 2500.5,
        'oil': 750.0
    }

    # Define explicit conversion factors for clarity in this context: 
    # Key is the assumed unit magnitude (e.g., liters = 1000), Value is factor to cubic meters.
    specific_factors = {1000.0: 0.001} 
    
    standardized_data = standardize_volume(raw_data, base_unit="cubic_meters", conversion_factors=specific_factors)

    print("Standardized Volume Measurements (in Cubic Meters):")
    for item, value in standardized_data.items():
        # Formatting to show reasonable precision without excessive decimals
        formatted_value = f"{value:.4f}" if isinstance(value, float) else str(value)
        print(f"  {item}: {formatted_value}")

    assert all(isinstance(v, (int, float)) for v in standardized_data.values()), "All values must be numeric."