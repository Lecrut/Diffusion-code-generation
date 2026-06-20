import argparse

CONVERSION_FACTORS = {
    'km': {'m': 1000, 'ft': 3280.84, 'mi': 0.621371},
    'm': {'km': 0.001, 'ft': 3.28084, 'mi': 0.000621371},
    'ft': {'km': 0.0003048, 'm': 0.3048, 'mi': 0.000189394},
    'mi': {'km': 1.60934, 'm': 1609.34, 'ft': 5280.0},
}

def convert_distance(distance, from_unit, to_unit):
    if from_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Invalid input unit: {from_unit}")
    if to_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Invalid output unit: {to_unit}")
    if from_unit == to_unit:
        return distance
    return distance * CONVERSION_FACTORS[from_unit][to_unit]

def main():
    parser = argparse.ArgumentParser(description='Convert distances between units.')
    parser.add_argument('dist1', type=float, help='First distance value')
    parser.add_argument('dist2', type=float, help='Second distance value')
    parser.add_argument('output_unit', type=str, choices=['km', 'm', 'ft', 'mi'], help='Desired output unit')
    args = parser.parse_args()

    try:
        result1 = convert_distance(args.dist1, 'km', args.output_unit)
        result2 = convert_distance(args.dist2, 'm', args.output_unit)
        print(f"{args.dist1} km = {result1}")
        print(f"{args.dist2} m = {result2}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()