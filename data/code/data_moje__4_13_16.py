import argparse
import sys

def convert_distance(distance1, distance2, output_unit):
    valid_units = ['m', 'km', 'ft', 'mi', 'cm', 'mm']
    if output_unit not in valid_units:
        raise ValueError(f"Invalid unit '{output_unit}'. Choose from {valid_units}")
    
    units_to_meters = {
        'm': 1,
        'km': 1000,
        'ft': 0.3048,
        'mi': 1609.34,
        'cm': 0.01,
        'mm': 0.001
    }
    
    meters_1 = distance1 * units_to_meters['m'] if distance1 else 0
    meters_2 = distance2 * units_to_meters['m'] if distance2 else 0
    total_meters = meters_1 + meters_2
    
    conversion_factor = units_to_meters[output_unit]
    result = total_meters / conversion_factor
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('d1', type=float, nargs='?', default=10.5)
    parser.add_argument('d2', type=float, nargs='?', default=20.0)
    parser.add_argument('unit', type=str, nargs='?', default='m')
    
    args = parser.parse_args(['10.5', '20.0', 'ft'])
    
    result = convert_distance(args.d1, args.d2, args.unit)
    print(result)