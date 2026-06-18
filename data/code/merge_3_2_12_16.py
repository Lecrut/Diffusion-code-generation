import math

# Predefined conversion factors to base unit: cubic meters (m^3)
CONVERSION_FACTORS = {
    'water': 1e-6,      # Assuming input is in liters; 1 liter = 0.001 m^3 -> adjusted for typical small volumes if needed, 
                        # but strictly following standard SI: 1 L = 1e-3 m^3. Let's correct this assumption to be explicit and robust.
    'sand': 5e-7        # Assuming input is in cubic centimeters (cm^3); 1 cm^3 = 1e-6 m^3
    
}

# Correction for realistic standard units based on typical measurement contexts:
CONVERSION_FACTORS_CORRECTED = {
    'water': 0.001,     # Input unit assumed to be Liters -> Cubic Meters (1 L = 0.001 m^3)
    'sand': 1e-6        # Input unit assumed to be cubic centimeters (cm^3) -> Cubic Meters (1 cm^3 = 1e-6 m^3)
}

def standardize_volume(input_dict: dict, conversion_factors=None) -> float:
    """
    Converts volume measurements in a dictionary to a standardized base unit.
    
    Args:
        input_dict (dict): Dictionary containing substance names as keys and volumes in various units as values.
                           Example: {'water': 10.0, 'sand': 5.5} where water is likely Liters and sand cm^3.
        conversion_factors (dict): Optional dictionary mapping unit strings to their multipliers for cubic meters.
                                  If None, uses the predefined default factors based on assumed input units per substance key.

    Returns:
        float: The total volume in standardized base units (cubic meters).

    Raises:
        ValueError: If a value in the input dictionary is not a number or if an unknown unit requires conversion and no factor exists.
    
    Note: 
        This function assumes specific default input units for keys like 'water' and 'sand'. 
        For robustness, it attempts to use provided factors; otherwise, it relies on internal defaults defined in CONVERSION_FACTORS_CORRECTED.
"""
    if conversion_factors is None:
        # Using the corrected predefined logic based on common measurement assumptions
        default_map = {k: v for k, v in CONVERSION_FACTORS_CORRECTED.items()}
    
    total_volume_m3 = 0.0
    
    for substance, value in input_dict.items():
        if not isinstance(value, (int, float)):
            raise ValueError(f"Invalid volume type '{value}' for substance '{substance}'. Expected numeric.")
            
        unit_key = str(substance).lower()
        
        # Determine conversion factor: use provided one or fallback to predefined defaults based on keys
        convert_factor = conversion_factors.get(unit_key) if conversion_factors else default_map[unit_key]
        
        try:
            converted_value = value * convert_factor
            total_volume_m3 += converted_value
            
        except Exception as e:
            raise ValueError(f"Error converting volume for '{substance}': {e}")

    return round(total_volume_m3, 6)

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    sample_data = {'water': 10.5, 'sand': 2500.0} 
    
    try:
        result = standardize_volume(sample_data)
        print(f"Standardized total volume in cubic meters: {result}")
        
        # Verification with explicit conversion factors for transparency (optional usage test)
        custom_factors = {'water': 1e-3, 'sand': 2.5e-6} 
        result_custom = standardize_volume(sample_data, custom_factors)
        print(f"Standardized total volume using custom factors: {result_custom}")
        
    except Exception as e:
        print(f"An error occurred during processing: {e}")