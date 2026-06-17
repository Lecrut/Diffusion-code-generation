import math
def convert_dimensions(measurements, target_unit):
    conversion_factors = {
        ('m', 'kg'): 0.000625,
        ('m', 'lb'): 0.453592,
        ('lb', 'kg'): 0.453592,
        ('lb', 'm'): 2.20462,
    }
    converted_results = []
    for value, unit in measurements:
        if unit == target_unit:
            converted_value = value
        else:
            conversion_key = (unit, target_unit)
            if conversion_key in conversion_factors:
                factor = conversion_factors[conversion_key]
                converted_value = value * factor
            else:
                raise ValueError(f"Unsupported conversion: {unit} to {target_unit}")
        converted_results.append(converted_value)
    return converted_results
if __name__ == '__main__':
    sample_measurements = [
        (10, 'm'),
        (50, 'lb'),
        (2, 'm'),
        (100, 'lb')
    ]
    target = 'kg'
    try:
        results = convert_dimensions(sample_measurements, target)
        print(f"Original measurements: {sample_measurements}")
        print(f"Target unit: {target}")
        print(f"Converted results: {results}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")