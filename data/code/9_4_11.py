import argparse
import sys

def convert_volume(value, from_unit, to_unit):
    units = {
        'ml': 1,
        'l': 1000,
        'gal': 3785.41178,
        'qt': 946.352946,
        'pt': 473.176473,
        'cup': 240,
        'oz': 29.5735
    }
    
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in units:
        raise ValueError(f"Unsupported starting unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    base_value = value * units[from_unit]
    result = base_value / units[to_unit]
    return result

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Convert volume units.')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('from_unit', type=str, help='The starting unit (e.g., l, ml, gal)')
    parser.add_argument('to_unit', type=str, help='The target unit (e.g., l, ml, gal)')
    return parser.parse_args(args)

def run_conversion(args_list=None):
    args = parse_args(args_list)
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    return result

if __name__ == '__main__':
    sample_values = ['5', 'gal', 'l']
    output = run_conversion(sample_values)
    print(output)