import argparse

def convert_distance(distance1, distance2, unit):
    valid_units = ['m', 'km', 'ft', 'mi']
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Valid units are {valid_units}")
    
    total_distance_meters = (distance1 if unit == 'm' else distance1 * 1000 if unit == 'km' 
                             else distance1 / 3.28084 if unit == 'ft' else distance1 * 1609.34)
    
    converted_distance = total_distance_meters + (distance2 if unit == 'm' else distance2 * 1000 if unit == 'km' 
                                                 else distance2 / 3.28084 if unit == 'ft' else distance2 * 1609.34)
    
    return converted_distance

if __name__ == '__main__':
    try:
        result = convert_distance(10, 5, 'km')
        print(result)
    except ValueError as e:
        print(e)