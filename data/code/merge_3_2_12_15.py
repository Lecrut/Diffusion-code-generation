import math

# Predefined conversion factors to cubic meters (m^3)
CONVERSION_FACTORS = {
    'water': 1e-6,      # Assuming input is in liters -> m^3 (1 L = 0.000001 m^3)
    'sand': 25e-7,      # Example specific factor for sand if needed, or generic volume unit conversion
}

def standardize_volume(volume_dict):
    """
    Converts a dictionary of volume measurements to cubic meters using predefined factors.
    
    Args:
        volume_dict (dict): A dictionary where keys are substance names and values are volumes in arbitrary units.
        
    Returns:
        dict: A new dictionary with all values converted to cubic meters.
    """
    standardized_data = {}
    
    for key, value in volume_dict.items():
        if isinstance(value, (int, float)):
            # Use the conversion factor from our predefined set; defaulting to 1e-6 if not found as a safety net
            factor = CONVERSION_FACTORS.get(key.lower(), 1.0) 
            standardized_data[key] = value * factor
        else:
            raise ValueError(f"Unsupported volume type for key '{key}'. Expected numeric value.")
            
    return standardized_data

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files)
    raw_volumes = {
        'water': 10.5,      # Liters assumed based on factor definition above
        'sand': 200,        # Arbitrary unit assuming specific sand density/volume context or generic scaling
        'oil': 3.7          # Another substance with a default fallback if not explicitly defined in factors dict for this demo
    }

    result = standardize_volume(raw_volumes)
    
    print("Standardized Volume Measurements (in cubic meters):")
    for item, vol_meters in result.items():
        print(f"{item}: {vol_meters:.6f} m^3")