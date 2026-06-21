import argparse
import sys

VALID_UNITS = ['cups', 'fluid_ounces', 'pints', 'quarts', 'gallons', 'tablespoons', 'teaspoons', 'milliliters', 'liters']

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'cups': 236.588,
        'fluid_ounces': 29.5735,
        'pints': 473.176,
        'quarts': 946.353,
        'gallons': 3785.41,
        'tablespoons': 14.7868,
        'teaspoons': 4.92892,
        'milliliters': 1.0,
        'liters': 1000.0
    }
    
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    if from_unit_lower not in conversion_factors:
        raise ValueError(f"Invalid input unit: {from_unit}")
    if to_unit_lower not in conversion_factors:
        raise ValueError(f"Invalid output unit: {to_unit}")
        
    value_in_ml = value * conversion_factors[from_unit_lower]
    result = value_in_ml / conversion_factors[to_unit_lower]
    return result

def main():
    parser = argparse.ArgumentParser(description='Convert volume between different units.')
    parser.add_argument('--value', type=float, required=True, help='The volume value to convert')
    parser.add_argument('--from-unit', type=str, required=True, help='The input unit')
    parser.add_argument('--to-unit', type=str, required=True, help='The desired output unit')
    
    args = parser.parse_args()
    
    try:
        result = convert_volume(args.value, args.from_unit, args.to_unit)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    sample_value = 2.0
    sample_from_unit = 'cups'
    sample_to_unit = 'milliliters'
    result = convert_volume(sample_value, sample_from_unit, sample_to_unit)
    print(result)