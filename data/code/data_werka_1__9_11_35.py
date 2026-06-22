def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic meters': 0.000001},
        'cubic meters': {'liters': 1000, 'milliliters': 1000000, 'cubic meters': 1}
    }
    
    try:
        conversion_factor = conversion_rates[source_unit][target_unit]
        converted_volume = volume * conversion_factor
        return converted_volume
    except KeyError:
        raise ValueError(f"Invalid unit: {source_unit} or {target_unit}")

if __name__ == '__main__':
    sample_volume = 2.5
    source_unit = 'liters'
    target_unit = 'milliliters'
    
    try:
        result = convert_volume(sample_volume, source_unit, target_unit)
        print(result)
    except ValueError as e:
        print(e)