import argparse

def convert_distance(distance1, distance2, unit):
    units = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    
    if unit not in units:
        raise ValueError(f"Invalid unit: {unit}. Please choose from {list(units.keys())}")
    
    total_distance_m = distance1 + distance2
    converted_distance = total_distance_m / units[unit]
    return converted_distance

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert two distances to a specified unit.')
    parser.add_argument('distance1', type=float, help='First distance in meters')
    parser.add_argument('distance2', type=float, help='Second distance in meters')
    parser.add_argument('unit', type=str, help='Desired output unit (m, km, cm, mm, in, ft, yd, mi)')
    
    args = parser.parse_args()
    
    try:
        result = convert_distance(args.distance1, args.distance2, args.unit)
        print(result)
    except ValueError as e:
        print(e)