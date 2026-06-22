import argparse
import sys

def convert_distances(distance1, distance2, output_unit):
    valid_units = ['km', 'm', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
    if output_unit not in valid_units:
        raise ValueError(f"Invalid unit '{output_unit}'. Choose from: {', '.join(valid_units)}")
    
    units_to_meters = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    
    total_meters = (distance1 * units_to_meters['km']) + (distance2 * units_to_meters['km'])
    result = total_meters / units_to_meters[output_unit]
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert two distances to a target unit.')
    parser.add_argument('distance1', type=float, nargs='?', default=1.5)
    parser.add_argument('distance2', type=float, nargs='?', default=2.5)
    parser.add_argument('output_unit', type=str, nargs='?', default='m')
    
    args = parser.parse_args(['1.5', '2.5', 'm'])
    
    result = convert_distances(args.distance1, args.distance2, args.output_unit)
    print(result)