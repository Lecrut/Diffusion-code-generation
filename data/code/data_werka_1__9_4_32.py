import argparse

def convert_volume(volume, from_unit, to_unit):
    conversion_factors = {'ml': {'l': 0.001, 'gal': 0.00264172}, 'l': {'ml': 1000, 'gal': 0.264172}, 'gal': {'ml': 3785.41, 'l': 3.78541}}
    if from_unit not in conversion_factors or to_unit not in conversion_factors[from_unit]:
        return 'Invalid unit conversion'
    factor = conversion_factors[from_unit][to_unit]
    converted_volume = volume * factor
    return converted_volume
if __name__ == '__main__':
    volume = 1000
    from_unit = 'ml'
    to_unit = 'l'
    result = convert_volume(volume, from_unit, to_unit)
    print(result)