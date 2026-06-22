import argparse

def convert_distance(distance1, distance2, unit):
    valid_units = ['m', 'km', 'ft', 'in']
    if unit not in valid_units:
        raise ValueError(f'Invalid unit: {unit}. Valid units are: {valid_units}')
    total_distance_meters = (distance1 + distance2) * 1000
    conversion_factors = {'m': 1, 'km': 0.001, 'ft': 3.28084, 'in': 39.3701}
    return total_distance_meters * conversion_factors[unit]
if __name__ == '__main__':
    distance1 = 500
    distance2 = 1000
    unit = 'km'
    try:
        result = convert_distance(distance1, distance2, unit)
        print(result)
    except ValueError as e:
        print(e)