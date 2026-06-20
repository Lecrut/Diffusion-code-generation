import argparse
import sys

CONVERSION_RATES = {
    'ml': 1,
    'l': 1000,
    'fl_oz': 29.5735,
    'cup': 236.588,
    'pt': 473.176,
    'qt': 946.353,
    'gal': 3785.41,
    'tsp': 4.92892,
    'tbsp': 14.7868,
    'in3': 16.3871,
    'ft3': 28316.8,
}

def convert_volume(amount, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in CONVERSION_RATES:
        raise ValueError(f"Unsupported starting unit: {from_unit}")
    if to_unit not in CONVERSION_RATES:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    base_value = amount * CONVERSION_RATES[from_unit]
    result = base_value / CONVERSION_RATES[to_unit]
    
    return result

def create_cli_parser():
    parser = argparse.ArgumentParser(description='Convert volume units.')
    parser.add_argument('--volume', type=float, required=True, help='The volume value to convert.')
    parser.add_argument('--from-unit', type=str, required=True, dest='from_unit', help='The starting unit (e.g., ml, l, gal).')
    parser.add_argument('--to-unit', type=str, required=True, dest='to_unit', help='The target unit (e.g., oz, cup, qt).')
    return parser

def run_conversion_cli(volume, from_unit, to_unit):
    result = convert_volume(volume, from_unit, to_unit)
    print(result)

if __name__ == '__main__':
    run_conversion_cli(1, 'gal', 'l')
    run_conversion_cli(250, 'ml', 'fl_oz')
    run_conversion_cli(1, 'tsp', 'ml')