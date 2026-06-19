import argparse

def convert_distance(distance1, distance2, unit):
    valid_units = ['m', 'km', 'ft', 'mi']
    if unit not in valid_units:
        raise ValueError(f'Invalid unit: {unit}. Valid units are {valid_units}')
    total_meters = (distance1 + distance2) * {'m': 1, 'km': 1000, 'ft': 0.3048, 'mi': 1609.34}[unit]
    return total_meters
if __name__ == '__main__':
    distance1 = 5
    distance2 = 10
    unit = 'km'
    try:
        result = convert_distance(distance1, distance2, unit)
        print(f'Total distance in {unit}: {result}')
    except ValueError as e:
        print(e)