CONVERSION_FACTORS = {
    'cubic_meter': 1.0,
    'cubic_centimeter': 1.0e-6,
    'liter': 1.0e-3,
    'milliliter': 1.0e-6,
    'cubic_foot': 0.0283168,
    'cubic_inch': 1.63871e-5,
    'gallon_us': 0.00378541,
    'quart_us': 9.46353e-4,
    'pint_us': 4.73176e-4,
    'fluid_ounce_us': 2.95735e-5
}

def standardize_volume(measurements: dict, base_unit: str = 'cubic_meter') -> dict:
    if base_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported base unit: {base_unit}")
    
    base_factor = CONVERSION_FACTORS[base_unit]
    standardized = {}
    
    for key, value in measurements.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value for {key} must be a number, got {type(value).__name__}")
        
        unit = key.split('_')[-1] if '_' in key else 'unknown'
        
        if unit not in CONVERSION_FACTORS:
            raise ValueError(f"Unknown unit: {unit} in key '{key}'")
        
        conversion_factor = CONVERSION_FACTORS[unit]
        standardized_value = value * conversion_factor / base_factor
        standardized[key] = standardized_value
    
    return standardized

if __name__ == '__main__':
    sample_data = {
        'water_cubic_meter': 2.5,
        'sand_liters': 1500.0,
        'oil_gallon_us': 50.0,
        'gravel_cubic_foot': 100.0
    }
    result = standardize_volume(sample_data, 'cubic_meter')
    print(result)