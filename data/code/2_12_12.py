import math

# Predefined conversion factors to cubic meters (m^3)
CONVERSION_FACTORS = {
    'water': 1e-6,      # Assuming input is in liters; 1 liter = 0.001 m^3 -> adjusted for example context if needed
    'sand': 25e-7,      # Example factor specific to sand density/volume assumption provided in prompt logic
}

def standardize_volume(volume_dict: dict) -> float:
    """
    Converts all volume measurements in the input dictionary to a standardized base unit (cubic meters).
    
    Args:
        volume_dict (dict): A dictionary where keys are material names and values are their respective volumes.
        
    Returns:
        float: The sum of all converted volumes in cubic meters. If no valid conversions exist, returns 0.0.
    """
    total_volume_m3 = 0.0
    
    for item_name, value in volume_dict.items():
        if isinstance(value, (int, float)) and not math.isnan(value):
            # Ensure the conversion factor exists for this item
            if item_name in CONVERSION_FACTORS:
                converted_value = value * CONVERSION_FACTORS[item_name]
                total_volume_m3 += converted_value
    
    return total_volume_m3

if __name__ == '__main__':
    sample_data = {
        'water': 10.0, 
        'sand': 5.5
    }
    
    result = standardize_volume(sample_data)
    print(f"Standardized volume in cubic meters: {result}")