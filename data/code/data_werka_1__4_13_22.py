import argparse

def convert_distance(distance1, distance2, output_unit):
    units = {'m': 1, 'km': 1000, 'cm': 100}
    
    if output_unit not in units:
        raise ValueError("Invalid unit. Please choose from 'm', 'km', or 'cm'.")
    
    total_distance_meters = (distance1 * units['m'] + distance2 * units['m'])
    converted_distance = total_distance_meters / units[output_unit]
    
    return converted_distance

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert two distances to a desired unit.')
    parser.add_argument('distance1', type=float, help='First distance')
    parser.add_argument('distance2', type=float, help='Second distance')
    parser.add_argument('output_unit', type=str, help='Desired output unit (m, km, cm)')
    
    args = parser.parse_args()
    
    try:
        result = convert_distance(args.distance1, args.distance2, args.output_unit)
        print(result)
    except ValueError as e:
        print(e)