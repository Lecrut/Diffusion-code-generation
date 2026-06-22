import argparse
import sys

def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'ml': 1.0,
        'l': 1000.0,
        'gal': 3785.41,
        'qt': 946.353,
        'pt': 473.176,
        'cup': 236.588,
        'floz': 29.5735,
        'tbsp': 14.7868,
        'tsp': 4.92892
    }
    
    if from_unit not in conversion_factors:
        raise ValueError(f"Unsupported input unit: {from_unit}")
    if to_unit not in conversion_factors:
        raise ValueError(f"Unsupported output unit: {to_unit}")
    
    if value < 0:
        raise ValueError("Volume cannot be negative")
    
    base_value = value * conversion_factors[from_unit]
    result = base_value / conversion_factors[to_unit]
    
    return result

def create_parser():
    parser = argparse.ArgumentParser(description="Convert volume units")
    parser.add_argument('--value', type=float, required=True, help="Input volume value")
    parser.add_argument('--from', dest='from_unit', type=str, required=True, help="Input unit")
    parser.add_argument('--to', dest='to_unit', type=str, required=True, help="Output unit")
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        result = convert_volume(args.value, args.from_unit, args.to_unit)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    result = convert_volume(1.0, 'gal', 'l')
    print(result)
    
    result = convert_volume(500, 'ml', 'cup')
    print(result)
    
    result = convert_volume(2.5, 'l', 'gal')
    print(result)