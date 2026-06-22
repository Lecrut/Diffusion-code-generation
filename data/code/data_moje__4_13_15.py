import argparse

VALID_UNITS = ['meters', 'kilometers', 'miles', 'feet']

UNIT_TO_METER_FACTOR = {
    'meters': 1.0,
    'kilometers': 1000.0,
    'miles': 1609.344,
    'feet': 0.3048
}

def convert_distance(distance, from_unit, to_unit):
    if from_unit not in UNIT_TO_METER_FACTOR:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in UNIT_TO_METER_FACTOR:
        raise ValueError(f"Invalid target unit: {to_unit}")
    
    distance_in_meters = distance * UNIT_TO_METER_FACTOR[from_unit]
    converted_distance = distance_in_meters / UNIT_TO_METER_FACTOR[to_unit]
    return converted_distance

def main():
    parser = argparse.ArgumentParser(description='Convert distances between units.')
    parser.add_argument('--dist1', type=float, required=True, help='First distance value')
    parser.add_argument('--unit1', type=str, required=True, help='Unit of the first distance')
    parser.add_argument('--dist2', type=float, required=True, help='Second distance value')
    parser.add_argument('--unit2', type=str, required=True, help='Unit of the second distance')
    parser.add_argument('--output-unit', type=str, required=True, help='Desired output unit')
    
    args = parser.parse_args()
    
    try:
        converted_dist1 = convert_distance(args.dist1, args.unit1, args.output_unit)
        converted_dist2 = convert_distance(args.dist2, args.unit2, args.output_unit)
        total_distance = converted_dist1 + converted_dist2
        print(total_distance)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    import sys
    sys.argv = ['script.py', '--dist1', '5', '--unit1', 'kilometers', '--dist2', '10', '--unit2', 'miles', '--output-unit', 'meters']
    main()