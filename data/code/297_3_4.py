import math
def convert_dimensions(measurements, target_unit):
    conversion_factors = {
        ('m', 'kg'): 0.000625,
        ('ft', 'kg'): 0.0220462,
        ('in', 'kg'): 0.000163871,
        ('lb', 'kg'): 0.453592,
        ('m', 'ft'): 3.28084,
        ('ft', 'm'): 0.3048,
        ('in', 'cm'): 2.54,
        ('cm', 'm'): 0.01,
    }
    converted_results = []
    for value, unit in measurements:
        if unit == target_unit:
            converted_value = value
        else:
            key = (unit, target_unit)
            if key in conversion_factors:
                factor = conversion_factors[key]
                converted_value = value * factor
            else:
                raise ValueError(f"Unsupported conversion: {unit} to {target_unit}")
        converted_results.append(converted_value)
    return converted_results
if __name__ == '__main__':
    sample_measurements = [
        (10, 'm'),
        (5, 'lb'),
        (120, 'cm'),
        (3, 'ft')
    ]
    target = 'kg'
    try:
        results = convert_dimensions(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print(f"Converted results: {results}")
    except ValueError as e:
        print(f"Error: {e}")