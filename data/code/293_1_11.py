def validate_input(value, unit):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError('Value must be a non-negative number')
    if unit not in ['km', 'mi']:
        raise ValueError("Unit must be 'km' or 'mi'")

def convert_distance(value, from_unit, to_unit):
    validate_input(value, from_unit)
    km_to_mi = 0.621371
    mi_to_km = 1 / km_to_mi
    if from_unit == 'km':
        return value * km_to_mi if to_unit == 'mi' else value
    elif from_unit == 'mi':
        return value * mi_to_km if to_unit == 'km' else value
if __name__ == '__main__':
    print(convert_distance(10, 'km', 'mi'))
    print(convert_distance(5, 'mi', 'km'))