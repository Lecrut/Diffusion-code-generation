import argparse

VALID_UNITS = ('m', 'km', 'ft', 'mi')

CONVERSION_TO_METERS = {
    'm': 1.0,
    'km': 1000.0,
    'ft': 0.3048,
    'mi': 1609.344
}

def convert_distance(distance_value, from_unit, to_unit):
    if from_unit not in CONVERSION_TO_METERS:
        raise ValueError(f"Invalid input unit: {from_unit}. Valid units are: {VALID_UNITS}")
    if to_unit not in CONVERSION_TO_METERS:
        raise ValueError(f"Invalid output unit: {to_unit}. Valid units are: {VALID_UNITS}")
    
    meters = distance_value * CONVERSION_TO_METERS[from_unit]
    converted = meters / CONVERSION_TO_METERS[to_unit]
    return converted

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert distances between units.')
    parser.add_argument('--distance1', type=float, required=True, help='First distance value')
    parser.add_argument('--unit1', type=str, required=True, help='Unit for first distance')
    parser.add_argument('--distance2', type=float, required=True, help='Second distance value')
    parser.add_argument('--unit2', type=str, required=True, help='Unit for second distance')
    parser.add_argument('--output_unit', type=str, required=True, help='Desired output unit')
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:
        d1_converted = convert_distance(args.distance1, args.unit1, args.output_unit)
        d2_converted = convert_distance(args.distance2, args.unit2, args.output_unit)
        total = d1_converted + d2_converted
        print(total)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import sys
    sys.argv = ['script', '--distance1', '1', '--unit1', 'km', '--distance2', '500', '--unit2', 'm', '--output_unit', 'm']
    main()