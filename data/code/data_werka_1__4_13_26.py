import argparse

def convert_distance(distance1, distance2, unit):
    valid_units = ['m', 'km', 'ft', 'in']
    conversion_factors = {
        'm': 1,
        'km': 1000,
        'ft': 3.28084,
        'in': 39.3701
    }
    
    if unit not in valid_units:
        raise ValueError(f"Invalid unit: {unit}. Valid units are {valid_units}")
    
    total_distance_meters = (distance1 + distance2) * conversion_factors['m']
    converted_distance = total_distance_meters / conversion_factors[unit]
    return converted_distance

if __name__ == '__main__':
    try:
        result = convert_distance(10, 20, 'km')
        print(result)
    except ValueError as e:
        print(e)