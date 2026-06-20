import argparse
import sys

def parse_and_convert(dist1, dist2, unit1, unit2, target_unit):
    units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
    }
    
    valid_units = set(units.keys())
    
    if unit1 not in valid_units:
        raise ValueError(f"Invalid unit: {unit1}")
    if unit2 not in valid_units:
        raise ValueError(f"Invalid unit: {unit2}")
    if target_unit not in valid_units:
        raise ValueError(f"Invalid target unit: {target_unit}")
    
    try:
        val1 = float(dist1)
        val2 = float(dist2)
    except (ValueError, TypeError):
        raise ValueError("Distance values must be numeric")
    
    total_meters = val1 * units[unit1] + val2 * units[unit2]
    result = total_meters / units[target_unit]
    
    return result

def main():
    parser = argparse.ArgumentParser(description="Convert and sum distances")
    parser.add_argument('--dist1', type=float, default=1.0)
    parser.add_argument('--unit1', type=str, default='km')
    parser.add_argument('--dist2', type=float, default=0.5)
    parser.add_argument('--unit2', type=str, default='m')
    parser.add_argument('--target', type=str, default='m')
    
    args = parser.parse_args()
    
    try:
        result = parse_and_convert(args.dist1, args.dist2, args.unit1, args.unit2, args.target)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    sample_dist1 = 1.0
    sample_unit1 = 'km'
    sample_dist2 = 500.0
    sample_unit2 = 'm'
    sample_target = 'm'
    
    result = parse_and_convert(sample_dist1, sample_dist2, sample_unit1, sample_unit2, sample_target)
    print(result)