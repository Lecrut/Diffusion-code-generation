def convert_distance(value, target_unit):
    if value < 0:
        raise ValueError('Distance cannot be negative')
    if target_unit not in ('km', 'm', 'cm', 'mm', 'mi', 'ft', 'in'):
        raise ValueError('Unsupported target unit')
    if target_unit == 'km':
        meters = value * 1000.0
    elif target_unit == 'm':
        meters = value
    elif target_unit == 'cm':
        meters = value / 100.0
    elif target_unit == 'mm':
        meters = value / 1000.0
    elif target_unit == 'mi':
        meters = value / 1609.344
    elif target_unit == 'ft':
        meters = value / 3.28084
    elif target_unit == 'in':
        meters = value / 39.3701
    if abs(meters) < 1e-15:
        return 0.0
    if target_unit == 'km':
        result = meters / 1000.0
    elif target_unit == 'm':
        result = meters
    elif target_unit == 'cm':
        result = meters * 100.0
    elif target_unit == 'mm':
        result = meters * 1000.0
    elif target_unit == 'mi':
        result = meters / 1609.344
    elif target_unit == 'ft':
        result = meters / 3.28084
    elif target_unit == 'in':
        result = meters / 39.3701
    return result
if __name__ == '__main__':
    sample_distance = 5000.0
    target = 'km'
    result = convert_distance(sample_distance, target)
    print(result)