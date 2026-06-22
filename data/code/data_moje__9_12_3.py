import argparse
import sys

UNITS = {
    'ml': 1.0,
    'milliliter': 1.0,
    'milliliters': 1.0,
    'l': 1000.0,
    'liter': 1000.0,
    'liters': 1000.0,
    'gal': 3785.411784,
    'gallon': 3785.411784,
    'gallons': 3785.411784,
    'qt': 946.352946,
    'quart': 946.352946,
    'quarts': 946.352946,
    'pt': 473.176473,
    'pint': 473.176473,
    'pints': 473.176473,
    'cup': 236.588236,
    'cups': 236.588236,
    'tbsp': 14.7867648,
    'tablespoon': 14.7867648,
    'tablespoons': 14.7867648,
    'tsp': 4.9289216,
    'teaspoon': 4.9289216,
    'teaspoons': 4.9289216,
    'floz': 29.5735295625,
    'fluidounce': 29.5735295625,
    'fluidounces': 29.5735295625,
    'm3': 1000000.0,
    'cubicmeter': 1000000.0,
    'cubicmeters': 1000000.0,
    'cm3': 1.0,
    'cubiccentimeter': 1.0,
    'cubiccentimeters': 1.0,
}

def convert_volume(volume, from_unit, to_unit):
    from_unit_key = from_unit.lower()
    to_unit_key = to_unit.lower()
    
    if from_unit_key not in UNITS:
        raise ValueError(f"Unknown input unit: {from_unit}")
    if to_unit_key not in UNITS:
        raise ValueError(f"Unknown output unit: {to_unit}")
        
    base_volume = volume * UNITS[from_unit_key]
    result_volume = base_volume / UNITS[to_unit_key]
    
    return result_volume

def main():
    parser = argparse.ArgumentParser(description='Convert volume between units.')
    parser.add_argument('volume', type=float, help='The volume value to convert.')
    parser.add_argument('from_unit', type=str, help='The input unit of volume.')
    parser.add_argument('to_unit', type=str, help='The desired output unit of volume.')
    
    try:
        args = parser.parse_args()
        result = convert_volume(args.volume, args.from_unit, args.to_unit)
        print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    sample_volume = 1.0
    sample_from_unit = 'gallon'
    sample_to_unit = 'liter'
    
    result = convert_volume(sample_volume, sample_from_unit, sample_to_unit)
    print(result)