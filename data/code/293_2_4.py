import math
def convert_to_imperial(measurements):
    imperial_measurements = {}
    if 'mass' in measurements:
        mass_kg = measurements['mass']
        mass_lbs = mass_kg * 2.2046226218
        imperial_measurements['mass_lbs'] = mass_lbs
    if 'length' in measurements:
        length_m = measurements['length']
        length_ft = length_m / 0.3048
        imperial_measurements['length_ft'] = length_ft
    if 'volume' in measurements:
        volume_m3 = measurements['volume']
        volume_gal = volume_m3 * 264.172
        imperial_measurements['volume_gal'] = volume_gal
    if 'temperature_celsius' in measurements:
        temp_fahrenheit = (measurements['temperature_celsius'] * 9/5) + 32
        imperial_measurements['temperature_fahrenheit'] = temp_fahrenheit
    return imperial_measurements
if __name__ == '__main__':
    sample_data = {
        'mass': 10,
        'length': 5,
        'volume': 1.5,
        'temperature_celsius': 25
    }
    converted_data = convert_to_imperial(sample_data)
    print(converted_data)