import argparse

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.24,
        'fluid_ounce': 0.0295735,
        'tablespoon': 0.0147868,
        'teaspoon': 0.00492892,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001,
    }
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported starting unit: {from_unit}")
    if to_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    liters = value * conversion_factors[from_unit]
    result = liters / conversion_factors[to_unit]
    return result

def create_parser():
    parser = argparse.ArgumentParser(description='Convert volume units.')
    parser.add_argument('--value', type=float, required=True, help='The volume value to convert.')
    parser.add_argument('--from', dest='from_unit', type=str, required=True, help='The starting unit.')
    parser.add_argument('--to', dest='to_unit', type=str, required=True, help='The target unit.')
    return parser

def main():
    sample_value = 1.0
    sample_from_unit = 'gallon'
    sample_to_unit = 'liter'
    result = convert_volume(sample_value, sample_from_unit, sample_to_unit)
    print(result)

if __name__ == '__main__':
    main()