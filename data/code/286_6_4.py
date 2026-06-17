import math
def convert_to_km(value, unit):
    if unit == 'km':
        return value
    elif unit == 'm':
        return value / 1000.0
    elif unit == 'cm':
        return value / 1000000.0
    elif unit == 'mi':
        return value * 1.609344
    elif unit == 'ft':
        return value * 0.0003048
    else:
        raise ValueError(f"Unknown unit: {unit}")
def process_measurements(measurements):
    kilometers = []
    for value, unit in measurements:
        try:
            km_value = convert_to_km(value, unit)
            kilometers.append(km_value)
        except ValueError as e:
            print(f"Skipping measurement due to error: {e}")
    return kilometers
if __name__ == '__main__':
    sample_measurements = [
        (1000, 'm'),
        (5, 'mi'),
        (250000, 'cm'),
        (10, 'ft'),
        (50, 'km'),
        (100, 'm')
    ]
    result = process_measurements(sample_measurements)
    print(result)