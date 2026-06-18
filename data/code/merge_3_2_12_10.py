import math

# Predefined conversion factors to cubic meters (m^3)
CONVERSION_FACTORS = {
    'water': 0.01,       # Assuming input is in liters -> m^3 (1 L = 0.001 m^3, adjusted for example context if needed, here using direct factor logic below)
    'sand': 0.025        # Example specific factors; actual usage depends on assumed input units per key name convention or explicit mapping
    
}

def standardize_volume(volume_dict):
    """
    Converts a dictionary of volume measurements to cubic meters based on predefined conversion factors.
    
    Args:
        volume_dict (dict): A dictionary where keys are material names and values are volumes in arbitrary assumed input units.
        
    Returns:
        dict: A new dictionary with all values converted to cubic meters using the CONVERSION_FACTORS mapping.
            
    Note: 
    The conversion logic assumes that for each key 'k' in volume_dict, the value is multiplied by CONVERSION_FACTORS[k].
    If a unit is not found in factors, it defaults to identity (no change) or raises an error depending on strictness;
    here we assume valid keys exist based on task description.
    
    Example: 
        Input: {'water': 10.0} -> Output: { 'water': 0.1 } if factor is 0.01
    
    """
    standardized = {}
    for material, value in volume_dict.items():
        # Ensure the conversion factor exists; default to 1.0 if missing (though task implies predefined)
        factor = CONVERSION_FACTORS.get(material, 1.0)
        
        # Apply conversion: result = original_value * factor
        converted_value = value * factor
        
        standardized[material] = converted_value
    
    return standardized

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_data = {'water': 10.0, 'sand': 5.5}
    
    result = standardize_volume(sample_data)
    
    print("Standardized Volume Measurements:")
    for material, vol in result.items():
        # Formatting to avoid excessive decimals if integers become floats naturally
        formatted_vol = round(vol, 6) 
        print(f"{material}: {formatted_vol} m^3")