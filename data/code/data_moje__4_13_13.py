import argparse
import sys

def convert_distance(dist1, dist2, output_unit):
    valid_units = ['m', 'km', 'cm', 'mm', 'ft', 'in', 'yd', 'mi']
    
    if output_unit not in valid_units:
        raise ValueError(f"Invalid unit '{output_unit}'. Must be one of {valid_units}")
    
    to_meters = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.34
    }
    
    meters = (dist1 + dist2) * to_meters[output_unit]
    
    from_meters = {
        'm': 1,
        'km': 0.001,
        'cm': 100,
        'mm': 1000,
        'ft': 3.28084,
        'in': 39.3701,
        'yd': 1.09361,
        'mi': 0.000621371
    }
    
    result = (dist1 + dist2) * from_meters[output_unit]
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert sum of two distances to a desired unit.')
    parser.add_argument('dist1', type=float, help='First distance value')
    parser.add_argument('dist2', type=float, help='Second distance value')
    parser.add_argument('unit', type=str, help='Desired output unit (m, km, cm, mm, ft, in, yd, mi)')
    
    args = parser.parse_args(['5', '10', 'ft'])
    
    try:
        result = convert_distance(args.dist1, args.dist2, args.unit)
        print(f"{result}")
    except ValueError as e:
        print(f"Error: {e}")