import argparse

def convert_distance(distance1, distance2, unit):
    valid_units = ['m', 'km', 'ft', 'mi']
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Valid units are {valid_units}")
    
    total_distance_meters = (distance1 if unit == 'm' else distance1 * 1000 if unit == 'km' 
                             else distance1 / 3.28084 if unit == 'ft' else distance1 * 1609.34)
    
    total_distance_meters += (distance2 if unit == 'm' else distance2 * 1000 if unit == 'km' 
                              else distance2 / 3.28084 if unit == 'ft' else distance2 * 1609.34)
    
    return total_distance_meters

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert and sum two distances in a specified unit.')
    parser.add_argument('distance1', type=float, help='The first distance value')
    parser.add_argument('distance2', type=float, help='The second distance value')
    parser.add_argument('unit', type=str, help='The unit of the distances (m, km, ft, mi)')
    
    args = parser.parse_args()
    
    try:
        result = convert_distance(args.distance1, args.distance2, args.unit)
        print(result)
    except ValueError as e:
        print(e)