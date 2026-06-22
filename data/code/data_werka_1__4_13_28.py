import argparse

def convert_distance(distance1, distance2, unit):
    valid_units = ['m', 'km', 'cm']
    if unit not in valid_units:
        raise ValueError(f'Invalid unit: {unit}. Valid units are: {valid_units}')
    total_distance_meters = (distance1 + distance2) * 100 if unit == 'cm' else (distance1 + distance2) / 1000 if unit == 'km' else distance1 + distance2
    return total_distance_meters

def main():
    parser = argparse.ArgumentParser(description='Convert and sum two distances in a specified unit.')
    parser.add_argument('distance1', type=float, help='First distance in meters')
    parser.add_argument('distance2', type=float, help='Second distance in meters')
    parser.add_argument('unit', type=str, choices=['m', 'km', 'cm'], help='Desired output unit (m, km, cm)')
    args = parser.parse_args()
    try:
        result = convert_distance(args.distance1, args.distance2, args.unit)
        print(result)
    except ValueError as e:
        print(e)
if __name__ == '__main__':
    distance1 = 100.0
    distance2 = 200.0
    unit = 'km'
    try:
        result = convert_distance(distance1, distance2, unit)
        print(result)
    except ValueError as e:
        print(e)