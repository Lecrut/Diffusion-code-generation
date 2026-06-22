import argparse
import sys

def convert_distance(distance1, distance2, unit):
    valid_units = ['meters', 'kilometers', 'miles', 'feet', 'yards']
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Choose from {valid_units}")
    
    unit_multiplier = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.34,
        'feet': 0.3048,
        'yards': 0.9144
    }
    
    base_unit = 'meters'
    factor_in = unit_multiplier[unit]
    
    total_base = (distance1 * factor_in) + (distance2 * factor_in)
    total_result = total_base / factor_in
    
    return total_result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--d1', type=float, required=True)
    parser.add_argument('--d2', type=float, required=True)
    parser.add_argument('--unit', type=str, required=True)
    
    try:
        args = parser.parse_args(['--d1', '1', '--d2', '2', '--unit', 'meters'])
        result = convert_distance(args.d1, args.d2, args.unit)
        print(result)
    except SystemExit:
        sys.exit(0)