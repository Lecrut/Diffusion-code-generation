import argparse
import sys

def convert_volume(value, start_unit, target_unit):
    units = {
        'ml': 1,
        'l': 1000,
        'tsp': 4.92892,
        'tbsp': 14.7868,
        'fl_oz': 29.5735,
        'cup': 236.588,
        'pt': 473.176,
        'qt': 946.353,
        'gal': 3785.41
    }
    
    start_unit_lower = start_unit.lower()
    target_unit_lower = target_unit.lower()
    
    if start_unit_lower not in units:
        raise ValueError(f"Unsupported start unit: {start_unit}")
    if target_unit_lower not in units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_ml = value * units[start_unit_lower]
    result = value_in_ml / units[target_unit_lower]
    
    return round(result, 6)

def main():
    parser = argparse.ArgumentParser(description='Convert volume between different units.')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('start_unit', type=str, help='The starting unit (e.g., ml, l, gal)')
    parser.add_argument('target_unit', type=str, help='The target unit (e.g., ml, l, gal)')
    
    args = parser.parse_args()
    
    result = convert_volume(args.volume, args.start_unit, args.target_unit)
    
    print(f"{args.volume} {args.start_unit} is equal to {result} {args.target_unit}")

if __name__ == '__main__':
    sys.argv = ['script_name', '5', 'l', 'gal']
    main()