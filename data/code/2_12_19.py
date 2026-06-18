import math

# Predefined conversion factors to cubic meters (m^3)
CONVERSION_FACTORS = {
    'water': 0.01,       # Example: liter -> m^3
    'sand': 25e-6,       # Example: mm^3 -> m^3
}

def standardize_volume(input_dict):
    """
    Converts a dictionary of volume measurements to cubic meters using predefined factors.
    
    Args:
        input_dict (dict): Dictionary where keys are substance names and values are original volumes.
        
    Returns:
        dict: New dictionary with all values converted to cubic meters.
    """
    standardized_data = {}
    for substance, volume in input_dict.items():
        if substance not in CONVERSION_FACTORS:
            raise ValueError(f"Unsupported conversion factor for '{substance}'.")
        normalized_volume = float(volume) * CONVERSION_FACTORS[substance]
        standardized_data[substance] = round(normalized_volume, 6) # Round to avoid floating point noise
    
    return standardized_data

if __name__ == '__main__':
    sample_volumes = {'water': 10.0, 'sand': 55e3} 
    print("Standardizing volumes...")
    result = standardize_volume(sample_volumes)
    for substance, vol in result.items():
        print(f"{substance}: {vol} m^3")