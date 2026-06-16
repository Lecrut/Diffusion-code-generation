import math
def convert_to_imperial(measurements):
    if 'mass' in measurements:
        mass_kg = measurements['mass']
        mass_lbs = mass_kg * 2.2046226218
        measurements['mass_lbs'] = mass_lbs
    if 'length' in measurements:
        length_m = measurements['length']
        length_ft = length_m / 0.3048
        measurements['length_ft'] = length_ft
    if 'volume' in measurements:
        volume_m3 = measurements['volume']
        volume_gal = volume_m3 * 264.172
        measurements['volume_gal'] = volume_gal
    return measurements
if __name__ == '__main__':
    sample_data = {'mass': 10, 'length': 5, 'volume': 1.5}
    converted_data = convert_to_imperial(sample_data.copy())
    print(converted_data)