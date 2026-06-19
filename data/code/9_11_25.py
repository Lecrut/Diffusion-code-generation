def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001}, 'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 1e-06}, 'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}}
    if source_unit not in conversion_rates or target_unit not in conversion_rates[source_unit]:
        raise ValueError('Invalid unit provided')
    return volume * conversion_rates[source_unit][target_unit]
if __name__ == '__main__':
    try:
        print(convert_volume(2, 'liters', 'milliliters'))
        print(convert_volume(1.5, 'cubic_meters', 'liters'))
        print(convert_volume(500, 'milliliters', 'cubic_meters'))
    except ValueError as e:
        print(e)