import argparse
import sys

UNITS = {
    'ml': {'name': 'milliliters', 'factor': 1.0},
    'l': {'name': 'liters', 'factor': 1000.0},
    'gal': {'name': 'gallons (US)', 'factor': 3785.41},
    'qt': {'name': 'quarts (US)', 'factor': 946.353},
    'pt': {'name': 'pints (US)', 'factor': 473.176},
    'cup': {'name': 'cups (US)', 'factor': 236.588},
    'floz': {'name': 'fluid ounces (US)', 'factor': 29.5735},
    'tbsp': {'name': 'tablespoons', 'factor': 14.7868},
    'tsp': {'name': 'teaspoons', 'factor': 4.92892},
}

def convert_volume(value, from_unit, to_unit):
    if from_unit not in UNITS:
        raise ValueError(f"Unknown input unit: {from_unit}")
    if to_unit not in UNITS:
        raise ValueError(f"Unknown output unit: {to_unit}")
    
    base_value = value * UNITS[from_unit]['factor']
    converted_value = base_value / UNITS[to_unit]['factor']
    return converted_value

def main():
    parser = argparse.ArgumentParser(description='Convert volume between units.')
    parser.add_argument('--value', type=float, required=True, help='Input volume value')
    parser.add_argument('--from-unit', type=str, required=True, help='Input unit (e.g., ml, l, gal)')
    parser.add_argument('--to-unit', type=str, required=True, help='Output unit (e.g., ml, l, gal)')
    
    try:
        args = parser.parse_args()
        result = convert_volume(args.value, args.from_unit.lower(), args.to_unit.lower())
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    sample_value = 2.5
    sample_from = 'gal'
    sample_to = 'l'
    sample_result = convert_volume(sample_value, sample_from, sample_to)
    print(sample_result)