import argparse

def convert_distance(distance1, distance2, output_unit):
    valid_units = ['m', 'km', 'ft', 'mi']
    if output_unit not in valid_units:
        raise ValueError(f'Invalid unit. Choose from {valid_units}')
    total_meters = (distance1 + distance2) * 1000
    conversion_factors = {'m': 1, 'km': 0.001, 'ft': 3280.84, 'mi': 0.000621371}
    converted_distance = total_meters * conversion_factors[output_unit]
    return converted_distance
if __name__ == '__main__':
    distance1 = 5.0
    distance2 = 3.0
    output_unit = 'm'
    try:
        result = convert_distance(distance1, distance2, output_unit)
        print(result)
    except ValueError as e:
        print(e)