import argparse

def convert_distance(distance, from_unit, to_unit):
    factors = {'m': 1.0, 'km': 1000.0, 'mi': 1609.34, 'ft': 0.3048}
    from_lower = from_unit.lower()
    to_lower = to_unit.lower()
    if from_lower not in factors:
        raise ValueError(f'Invalid input unit: {from_unit}')
    if to_lower not in factors:
        raise ValueError(f'Invalid output unit: {to_unit}')
    value_in_meters = distance * factors[from_lower]
    converted_value = value_in_meters / factors[to_lower]
    return converted_value

def main():
    parser = argparse.ArgumentParser(description='Convert distance between units.')
    parser.add_argument('distance1', type=float, help='First distance value.')
    parser.add_argument('distance2', type=float, help='Second distance value.')
    parser.add_argument('output_unit', type=str, help='Desired output unit (m, km, mi, ft).')
    args = parser.parse_args(['1000.0', '5000.0', 'km'])
    try:
        result1 = convert_distance(args.distance1, 'm', args.output_unit)
        result2 = convert_distance(args.distance2, 'm', args.output_unit)
        print(result1)
        print(result2)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    main()