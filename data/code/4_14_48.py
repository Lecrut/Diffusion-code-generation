def validate_unit(unit):
    supported_units = {'meters', 'kilometers', 'miles'}
    if unit not in supported_units:
        raise ValueError(f"Unsupported unit: {unit}")

def convert_to_meters(value, unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34
    }
    return value * conversion_factors[unit]

def normalize_distance(distance, unit):
    validate_unit(unit)
    return convert_to_meters(distance, unit)

if __name__ == '__main__':
    sample_values = [
        (15, 'meters'),
        (3, 'kilometers'),
        (1, 'miles')
    ]
    for value, unit in sample_values:
        normalized_value = normalize_distance(value, unit)
        print(f'{value} {unit} is {normalized_value} meters')