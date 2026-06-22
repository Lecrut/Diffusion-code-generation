conversion_factors = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}

def validate_unit(unit):
    if unit not in conversion_factors:
        raise ValueError(f'Invalid unit: {unit}. Supported units are s, m, h, d, w.')

def convert_time(value, from_unit, to_unit):
    validate_unit(from_unit)
    validate_unit(to_unit)
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])
if __name__ == '__main__':
    print(convert_time(1, 'h', 'm'))
    print(convert_time(24, 'd', 's'))
    print(convert_time(7, 'w', 'hours'))