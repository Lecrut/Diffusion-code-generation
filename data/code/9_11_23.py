def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {'liters': {'ml': 1000, 'l': 1, 'gal': 0.264172}, 'ml': {'ml': 1, 'l': 0.001, 'gal': 0.000264172}, 'gal': {'ml': 3785.41, 'l': 3.78541, 'gal': 1}}
    if source_unit not in conversion_rates:
        return 'Error: Unsupported source unit'
    if target_unit not in conversion_rates[source_unit]:
        return 'Error: Unsupported target unit'
    return volume * conversion_rates[source_unit][target_unit]
if __name__ == '__main__':
    print(convert_volume(10, 'ml', 'l'))
    print(convert_volume(5, 'liters', 'gal'))
    print(convert_volume(2, 'gal', 'ml'))
    print(convert_volume(100, 'l', 'unknown_unit'))