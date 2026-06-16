import math
def convert_to_base(value, unit):
    conversions = {
        'length': {
            'meter': 1.0,
            'kilometer': 1000.0,
            'centimeter': 0.01,
            'millimeter': 0.001,
            'inch': 0.0254,
            'foot': 0.3048,
            'mile': 1609.34
        },
        'mass': {
            'kilogram': 1.0,
            'gram': 0.001,
            'milligram': 0.000001,
            'pound': 0.453592,
            'ounce': 0.0283495
        },
        'volume': {
            'cubic_meter': 1.0,
            'liter': 0.001,
            'milliliter': 0.001,
            'cubic_centimeter': 0.000001
        }
    }
    if unit in conversions:
        if 'length' in conversions[unit]:
            return value * conversions[unit]['meter']
        elif 'mass' in conversions[unit]:
            return value * conversions[unit]['kilogram']
        elif 'volume' in conversions[unit]:
            return value * conversions[unit]['cubic_meter']
    return value
if __name__ == '__main__':
    print("--- Length Conversions ---")
    length_value = 10
    length_unit = "kilometer"
    result_length = convert_to_base(length_value, length_unit)
    print(f"{length_value} {length_unit} is equal to {result_length} meters")
    length_value = 500
    length_unit = "centimeter"
    result_length = convert_to_base(length_value, length_unit)
    print(f"{length_value} {length_unit} is equal to {result_length} meters")
    length_value = 10
    length_unit = "inch"
    result_length = convert_to_base(length_value, length_unit)
    print(f"{length_value} {length_unit} is equal to {result_length} meters")
    print("\n--- Mass Conversions ---")
    mass_value = 2.5
    mass_unit = "pound"
    result_mass = convert_to_base(mass_value, mass_unit)
    print(f"{mass_value} {mass_unit} is equal to {result_mass} kilograms")
    mass_value = 500
    mass_unit = "gram"
    result_mass = convert_to_base(mass_value, mass_unit)
    print(f"{mass_value} {mass_unit} is equal to {result_mass} kilograms")
    print("\n--- Volume Conversions ---")
    volume_value = 2
    volume_unit = "liter"
    result_volume = convert_to_base(volume_value, volume_unit)
    print(f"{volume_value} {volume_unit} is equal to {result_volume} cubic meters")