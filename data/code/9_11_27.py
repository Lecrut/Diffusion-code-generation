def convert_volume(volume, source_unit, target_unit='liter'):
    conversion_rates = {'liter': {'ml': 1000, 'l': 1, 'gal': 0.264172}, 'ml': {'ml': 1, 'l': 0.001, 'gal': 0.000264172}, 'gal': {'ml': 3785.41, 'l': 3.78541, 'gal': 1}}
    try:
        if source_unit not in conversion_rates or target_unit not in conversion_rates[source_unit]:
            raise ValueError('Invalid unit provided')
        conversion_factor = conversion_rates[source_unit][target_unit]
        converted_volume = volume * conversion_factor
        return converted_volume
    except TypeError:
        raise TypeError('Volume must be a number')
if __name__ == '__main__':
    print(convert_volume(10, 'liter'))
    print(convert_volume(500, 'ml', 'gal'))