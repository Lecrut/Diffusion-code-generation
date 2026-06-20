CONVERSION_TO_CUBIC_METERS = {
    'liters': 0.001,
    'milliliters': 1e-6,
    'gallons': 0.00378541,
    'cubic_feet': 0.0283168,
    'cubic_meters': 1.0,
    'water': 1.0,
    'sand': 1.0
}

def standardize_volume(volumes, base_unit='cubic_meters'):
    standardized = {}
    for substance, volume in volumes.items():
        unit = get_unit_for_substance(substance)
        if unit in CONVERSION_TO_CUBIC_METERS:
            converted_to_base = volume * CONVERSION_TO_CUBIC_METERS[unit]
            standardized[substance] = converted_to_base
        else:
            standardized[substance] = volume
    return standardized

def get_unit_for_substance(substance):
    if substance in CONVERSION_TO_CUBIC_METERS:
        return substance
    for unit in CONVERSION_TO_CUBIC_METERS:
        if substance.endswith(unit):
            return unit
    return 'liters'

if __name__ == '__main__':
    sample_volumes = {
        'water': 10.0,
        'sand': 5.5,
        'oil_in_liters': 200.0,
        'gas_in_gallons': 50.0
    }
    result = standardize_volume(sample_volumes)
    print(result)