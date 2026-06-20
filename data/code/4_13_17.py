import argparse

VALID_UNITS = ['meters', 'kilometers', 'miles', 'feet']

CONVERSION_TO_METERS = {
    'meters': 1.0,
    'kilometers': 1000.0,
    'miles': 1609.344,
    'feet': 0.3048
}

def parse_arguments():
    parser = argparse.ArgumentParser(description='Distance Unit Converter')
    parser.add_argument('distance1', type=float, help='First distance value')
    parser.add_argument('distance2', type=float, help='Second distance value')
    parser.add_argument('--unit', type=str, help='Desired output unit')
    args = parser.parse_args()
    return args

def validate_unit(unit):
    if unit not in VALID_UNITS:
        raise ValueError(f"Invalid unit: {unit}. Valid units are: {', '.join(VALID_UNITS)}")
    return unit

def convert_distance(distance, from_unit, to_unit):
    distance_in_meters = distance * CONVERSION_TO_METERS[from_unit]
    return distance_in_meters / CONVERSION_TO_METERS[to_unit]

def sum_distances(dist1, dist2, unit1, unit2, output_unit):
    dist1_in_meters = dist1 * CONVERSION_TO_METERS[unit1]
    dist2_in_meters = dist2 * CONVERSION_TO_METERS[unit2]
    total_meters = dist1_in_meters + dist2_in_meters
    return total_meters / CONVERSION_TO_METERS[output_unit]

def main():
    dist1 = 5.0
    dist2 = 10.0
    output_unit = 'kilometers'
    
    try:
        validate_unit(output_unit)
        result = sum_distances(dist1, dist2, 'meters', 'meters', output_unit)
        print(result)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()