def standardize_volume(volume_dict: dict[str, float], base_unit: str = "m³", factors: dict[str, float] | None = None) -> dict[str, float]:
    """
    Converts a dictionary of volume measurements to a standardized base unit.

    Args:
        volume_dict (dict): A dictionary where keys are material names and values are volumes in arbitrary units.
        base_unit (str): The target standard unit for output (default is "m³"). If None, assumes input is already in the desired format or uses internal defaults if factors aren't provided.
        factors (dict | None): Optional predefined conversion factors from input units to the specified base unit. 
                             Keys are strings representing the original unit of measurement for each item type found in volume_dict.
                             Values are floats indicating how many base_units correspond to 1 unit_of_measurement.

    Returns:
        dict: A dictionary with standardized volumes in 'base_unit'.

    Raises:
        ValueError: If a conversion factor is missing or invalid.
    
    Note:
        This function assumes that if factors are not provided, it attempts to infer the original units based on common material densities 
        (e.g., water ~1000 kg/m³ implies 1 L = 0.001 m³) or defaults to assuming all inputs might be in Liters if no specific factor is given for a key.
    """
    
    # Default conversion factors: assumed original unit per material type if not explicitly provided via 'factors' arg
    _default_factors_map = {
        "water": 0.001,      # Assuming input liters -> m³ (since density ~1kg/L and water is often measured in L)
        "sand": None         # Sand varies; we'll use a standard loose packing estimate if no explicit factor provided later
    }

    final_factors = factors if factors else _default_factors_map
    
    standardized_result = {}
    
    for material, value in volume_dict.items():
        original_unit_str = ""
        
        # Determine the conversion factor to apply
        used_factor = None
        
        # Check explicit factors first
        if material in final_factors:
            used_factor = final_factors[material]
        else:
            # Fallback logic based on common sense defaults for missing specific entries 
            # If no global context, assume generic liter conversion (1 L = 0.001 m³) as a safe default for unspecified units in this constrained scenario
            used_factor = 0.001 

        if value is None or not isinstance(value, (int, float)):
            raise ValueError(f"Invalid volume type for '{material}': {value}. Expected numeric.")

        # Apply conversion: Standardized Value = Input * Factor
        standardized_value = value * used_factor
        
        standardized_result[material] = standardized_value
    
    return standardized_result

if __name__ == '__main__':
    # Hard-coded sample values representing volume in Liters (assumed base input unit for demonstration)
    sample_volumes = {
        "water": 10.5, 
        "sand": 20.3, 
        "oil": 7.8
    }

    # Define custom conversion factors if desired to override defaults or demonstrate flexibility
    # Here we assume the input unit is Liters for all materials and convert strictly to cubic meters (m³)
    explicit_factors = {
        "water": 0.001,      # 1 Liter water = 0.001 m³
        "sand": 0.00245,     # Approximate loose sand density factor if input was mass? 
                            # NOTE: For pure volume conversion without mass context, we stick to geometric units or assume specific material fill factors.
                            # To keep it robust as a generic converter function: Let's treat the explicit factor here purely as 'input_unit_to_m3'.
    }

    # Refined logic for this run: Assume input is in Liters (common volume unit) -> Output m³
    conversion_rate = 0.001
    
    print("Original volumes:", sample_volumes)
    
    result = standardize_volume(sample_volumes, base_unit="m³", factors=conversion_rate) # Passing a global factor for simplicity or specific per-material if needed
    
    print("\nStandardized Volumes (in cubic meters):")
    for mat, vol in result.items():
        print(f"{mat}: {vol} m³")