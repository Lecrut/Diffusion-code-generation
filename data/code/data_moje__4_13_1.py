import argparse

def convert_distance(distance1, distance2, unit1, unit2):
    units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.34,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144
    }
    
    if unit1 not in units:
        raise ValueError(f"Invalid unit: {unit1}")
    if unit2 not in units:
        raise ValueError(f"Invalid unit: {unit2}")
        
    total_distance_in_meters = distance1 * units[unit1] + distance2 * units[unit1]
    result_in_target_unit = total_distance_in_meters / units[unit2]
    
    return result_in_target_unit

def create_parser():
    parser = argparse.ArgumentParser(description='Convert and add two distances.')
    parser.add_argument('--distance1', type=float, required=True, help='First distance value')
    parser.add_argument('--distance2', type=float, required=True, help='Second distance value')
    parser.add_argument('--unit1', type=str, required=True, help='Unit of the input distances')
    parser.add_argument('--unit2', type=str, required=True, help='Desired output unit')
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args(['--distance1', '10', '--distance2', '5', '--unit1', 'm', '--unit2', 'km'])
    
    try:
        result = convert_distance(args.distance1, args.distance2, args.unit1, args.unit2)
        print(result)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()