import math
def convert_dimensions(measurements, target_unit, conversion_factors):
    converted_measurements = []
    for value, unit in measurements:
        if unit == target_unit:
            converted_value = value
        else:
            try:
                value_in_base = value * conversion_factors[unit]
                converted_value = value_in_base
            except KeyError:
                raise ValueError(f"Unknown unit encountered: {unit}")
        converted_measurements.append(converted_value)
    return converted_measurements
if __name__ == '__main__':
    sample_measurements = [
        (10, 'meter'),
        (20, 'pound'),
        (5, 'meter'),
        (100, 'ounce')
    ]
    target = 'kilogram'
    conversion_factors = {
        'meter_to_kg': 0.000621371,
        'pound_to_kg': 0.453592,
        'ounce_to_kg': 0.0283495
    }
    try:
        results = convert_dimensions(sample_measurements, target, conversion_factors)
        print(results)
    except ValueError as e:
        print(f"Error: {e}")