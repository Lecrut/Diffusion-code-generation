def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001}, 'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 1e-06}, 'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}}
    if source_unit not in conversion_rates:
        raise ValueError(f'Unsupported source unit: {source_unit}')
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f'Unsupported target unit: {target_unit}')
    return volume * conversion_rates[source_unit][target_unit]
if __name__ == '__main__':
    print(convert_volume(5, 'liters', 'milliliters'))
    print(convert_volume(2.5, 'cubic_meters', 'liters'))
    print(convert_volume(1000, 'milliliters', 'cubic_meters'))