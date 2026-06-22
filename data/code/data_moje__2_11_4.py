CONVERSION_TO_CUBIC_METERS = {
    'liters': 0.001,
    'milliliters': 0.000001,
    'gallons': 0.00378541,
    'cubic_feet': 0.0283168,
    'cubic_meters': 1.0
}

DEFAULT_UNIT = 'cubic_meters'

def standardize_volume(volume_dict, unit_map=None, target_unit=DEFAULT_UNIT):
    if unit_map is None:
        unit_map = CONVERSION_TO_CUBIC_METERS

    result = {}
    for substance, value in volume_dict.items():
        if not isinstance(substance, str) or not isinstance(value, (int, float)):
            raise ValueError("Invalid entry in volume dictionary")
        
        substance_lower = substance.lower()
        
        if substance_lower not in unit_map:
            raise KeyError(f"Unknown unit: {substance}")
        
        conversion_factor = unit_map[substance_lower]
        standardized_value = value * conversion_factor
        result[substance] = standardized_value
        
    return result

if __name__ == '__main__':
    sample_data = {'water': 10.0, 'sand': 5.5, 'oil': 2.3}
    print(standardize_volume(sample_data))